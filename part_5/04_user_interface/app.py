# Copyright (c) The SkillPedia under Apache License 2.0 (see LICENSE.txt).
# Source for "Building a Large Language Model From Scratch"
#   
# Code: https://github.com/Sangwan70/Building-an-LLM-From-Scratch

from pathlib import Path
import sys

import tiktoken
import torch
import chainlit

from previous_parts import (
    classify_review,
    GPTModel
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def get_model_and_tokenizer():
    """
    Code to load finetuned GPT-2 model generated in part 5.
    This requires that you run the code in part 5 first, which generates the necessary model.pth file.
    """

    GPT_CONFIG_355M = {
        "vocab_size": 50257,     # Vocabulary size
        "context_length": 1024,  # Context length
        "emb_dim": 1024,          # Embedding dimension
        "n_heads": 16,           # Number of attention heads
        "n_layers": 24,          # Number of layers
        "drop_rate": 0.1,        # Dropout rate
        "qkv_bias": True         # Query-key-value bias
    }

    tokenizer = tiktoken.get_encoding("gpt2")

    model_path = Path("../..") / "gpt2" / "review_classifier.pth"
    if not model_path.exists():
        print(
            f"""Could not find the {model_path} file. Please run the part 5 code
             (part_5.ipynb) to generate the review_classifier.pth file."""
        )
        sys.exit()

    # Instantiate model
    model = GPTModel(GPT_CONFIG_355M)

    # Convert model to classifier as in section 5.5 in part_5.ipynb
    num_classes = 2
    model.out_head = torch.nn.Linear(in_features=GPT_CONFIG_355M["emb_dim"], out_features=num_classes)

    # Then load model weights
    checkpoint = torch.load(model_path, map_location=device, weights_only=True)
    model.load_state_dict(checkpoint)
    model.to(device)
    model.eval()

    return tokenizer, model


# Obtain the necessary tokenizer and model files for the chainlit function below
tokenizer, model = get_model_and_tokenizer()


@chainlit.on_message
async def main(message: chainlit.Message):
    """
    The main Chainlit function.
    """
    user_input = message.content

    label = classify_review(user_input, model, tokenizer, device, max_length=120)

    await chainlit.Message(
        content=f"{label}",  # This returns the model response to the interface
    ).send()