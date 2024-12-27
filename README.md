# Building a Large Language Model From Scratch

This repository contains the code for developing, pretraining, and finetuning a GPT-like LLM.

<br>
You'll learn and understand how large language models (LLMs) work from the inside out by coding them from the ground up, step by step. I'll guide you through creating your own LLM, explaining each stage with clear text, diagrams, and examples.

The method described for training and developing your own small-but-functional model for educational purposes mirrors the approach used in creating large-scale foundational models such as those behind ChatGPT. In addition, this repository includes code for loading the weights of larger pretrained models for finetuning.

- Link to the official [Source Code](https://github.com/Sangwan70/Building-an-LLM-From-Scratch)

<br>

```bash
git clone --depth 1 https://github.com/Sangwan70/Building-an-LLM-From-Scratch.git
```
<br>

# Table of Contents

<br>
<!--  -->

> [!TIP]
> If you're seeking guidance on installing Python and Python packages and setting up your code environment, I suggest reading the [README.md](setup/README.md) file located in the [setup](setup) directory.

<br>

| part Title                                              | Main Code (for Quick Access)                                                                                                    | All Code + Supplementary      |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| [Setup recommendations](setup)                             | -                                                                                                                               | -                             |
| Part 1: Working with Text Data                               | - [Part 1: Working with Text](part_1/01_main-code/part_1.ipynb)<br/>- [dataloader.ipynb](part_1/01_main-code/dataloader.ipynb) (summary)<br/>- [additional_examples.ipynb](part_1/01_main-code/additional_examples.ipynb)               | [./part_1](./part_1)            |
| Part 2: Coding Attention Mechanisms                          | - [Part 2: Coding Attention Mechanisms](part_2/01_main-code/part_2.ipynb)<br/>- [multihead-attention.ipynb](part_2/01_main-code/multihead-attention.ipynb) (summary) <br/>- [additional_examples.ipynb](part_2/01_main-code/additional_examples.ipynb)| [./part_2](./part_2)             |
| Part 3: Implementing a GPT Model from Scratch                | - [Part 3: Implementing a GPT model from Scratch](part_3/01_main-code/part_3.ipynb)<br/>- [gpt.py](part_3/01_main-code/gpt.py) (summary)<br/>- [additional_examples.ipynb](part_3/01_main-code/additional_examples.ipynb) | [./part_3](./part_3)           |
| Part 4: Pretraining on Unlabeled Data                        | - [Part 4: Pretraining on Unlabeled Data](part_4/01_main-code/part_4.ipynb)<br/>- [gpt_train.py](part_4/01_main-code/gpt_train.py) (summary) <br/>- [gpt_generate.py](part_4/01_main-code/gpt_generate.py) (summary) <br/>- [additional_examples.ipynb](part_4/01_main-code/additional_examples.ipynb) | [./part_4](./part_4)              |
| Part 5: Finetuning for Text Classification                   | - [Part 5: Finetuning for Text Classification](part_5/01_main-code/part_5.ipynb)  <br/>- [gpt_class_finetune.py](part_5/01_main-code/gpt_class_finetune.py)  <br/>- [additional_examples.ipynb](part_5/01_main-code/additional_examples.ipynb) | [./part_5](./part_5)              |
| Part 6: Finetuning to Follow Instructions                    | - [Part 6: Finetuning To Follow Instructions](part_6/01_main-code/part_6.ipynb)<br/>- [gpt_instruction_finetuning.py](part_6/01_main-code/gpt_instruction_finetuning.py) (summary)<br/>- [ollama_evaluate.py](part_6/01_main-code/ollama_evaluate.py) (summary)<br/>- [example-solutions.ipynb](part_6/01_main-code/example-solutions.ipynb) | [./part_6](./part_6)  |
| Appendix A: Introduction to PyTorch                        | - [code-part1.ipynb](appendix-A/01_main-code/code-part1.ipynb)<br/>- [code-part2.ipynb](appendix-A/01_main-code/code-part2.ipynb)<br/>- [DDP-script.py](appendix-A/01_main-code/DDP-script.py)<br/>- [additional_examples.ipynb](appendix-A/01_main-code/additional_examples.ipynb) | [./appendix-A](./appendix-A) |
| Appendix B: Adding Bells and Whistles to the Training Loop | - [appendix-B.ipynb](appendix-B/01_main-code/appendix-B.ipynb)                                                          | [./appendix-B](./appendix-B)  |
| Appendix C: Parameter-efficient Finetuning with LoRA       | - [appendix-C.ipynb](appendix-C/01_main-code/appendix-C.ipynb)                                                          | [./appendix-C](./appendix-C) |

<br>
&nbsp;

## Hardware Requirements

The code in the main parts of this course is designed to run on conventional laptops within a reasonable timeframe and does not require specialized hardware. Additionally, the code automatically utilizes GPUs if they are available. (Please see the [setup](https://github.com/Sangwan70/Building-an-LLM-From-Scratch/blob/main/setup/README.md) doc for additional recommendations.)

&nbsp;
## Additional Material

Several folders contain additional materials for interested readers:

- **Setup**
  - [Python Setup Tips](setup/01_optional-python-setup-preferences)
  - [Installing Python Packages and Libraries Used in this course](setup/02_installing-python-libraries)
  - [Docker Environment Setup Guide](setup/03_optional-docker-environment)
- **Part 1: Working with text data**
  - [Comparing Various Byte Pair Encoding (BPE) Implementations](part_1/02_bonus_bytepair-encoder)
  - [Understanding the Difference Between Embedding Layers and Linear Layers](part_1/03_bonus_embedding-vs-matmul)
  - [Dataloader Intuition with Simple Numbers](part_1/04_bonus_dataloader-intuition)
- **Part 2: Coding attention mechanisms**
  - [Comparing Efficient Multi-Head Attention Implementations](part_2/02_bonus_efficient-multihead-attention/mha-implementations.ipynb)
  - [Understanding PyTorch Buffers](part_2/03_understanding-buffers/understanding-buffers.ipynb)
- **Part 3: Implementing a GPT model from scratch**
  - [FLOPS Analysis](part_3/02_performance-analysis/flops-analysis.ipynb)
- **Part 4: Pretraining on unlabeled data:**
  - [Alternative Weight Loading from Hugging Face Model Hub using Transformers](part_4/02_alternative_weight_loading/weight-loading-hf-transformers.ipynb)
  - [Pretraining GPT on the Project Gutenberg Dataset](part_4/03_bonus_pretraining_on_gutenberg)
  - [Adding Bells and Whistles to the Training Loop](part_4/04_learning_rate_schedulers)
  - [Optimizing Hyperparameters for Pretraining](part_4/05_bonus_hparam_tuning)
  - [Building a User Interface to Interact With the Pretrained LLM](part_4/06_user_interface)
  - [Converting GPT to Llama](part_4/07_gpt_to_llama)
  - [Llama 3.2 From Scratch](part_4/07_gpt_to_llama/standalone-llama32.ipynb)
  - [Memory-efficient Model Weight Loading](part_4/08_memory_efficient_weight_loading/memory-efficient-state-dict.ipynb)
- **Part 5: Finetuning for classification**
  - [Additional experiments finetuning different layers and using larger models](part_5/02_bonus_additional-experiments)
  - [Finetuning different models on 50k IMDB movie review dataset](part_5/03_bonus_imdb-classification)
  - [Building a User Interface to Interact With the GPT-based Spam Classifier](part_5/04_user_interface)
- **Part 6: Finetuning to follow instructions**
  - [Dataset Utilities for Finding Near Duplicates and Creating Passive Voice Entries](part_6/02_dataset-utilities)
  - [Evaluating Instruction Responses Using the OpenAI API and Ollama](part_6/03_model-evaluation)
  - [Generating a Dataset for Instruction Finetuning](part_6/05_dataset-generation/llama3-ollama.ipynb)
  - [Improving a Dataset for Instruction Finetuning](part_6/05_dataset-generation/reflection-gpt4.ipynb)
  - [Generating a Preference Dataset with Llama 3.2 3B and Ollama](part_6/04_preference-tuning-with-dpo/create-preference-data-ollama.ipynb)
  - [Direct Preference Optimization (DPO) for LLM Alignment](part_6/04_preference-tuning-with-dpo/dpo-from-scratch.ipynb)
  - [Building a User Interface to Interact With the Instruction Finetuned GPT Model](part_6/06_user_interface)

<br>

## Questions, Feedback, and Contributing to This Repository


I welcome all sorts of feedback via [GitHub Discussions](https://github.com/Sangwan70/Building-an-LLM-From-Scratch/discussions). Likewise, if you have any questions or just want to bounce ideas off others, please don't hesitate to post these in the forum as well.

&nbsp;
## Citation

BibTeX entry:

```
  author       = {Ram N Sangwan},
  title        = {Building An LLM From Scratch}
  github       = {https://github.com/Sangwan70/Building-an-LLM-From-Scratch}
}
```
