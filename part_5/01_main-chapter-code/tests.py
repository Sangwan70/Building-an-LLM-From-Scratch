# Copyright (c) The SkillPedia under Apache License 2.0 (see LICENSE.txt).
# Source for "Build a Large Language Model From Scratch"
#   
# Code: 

# File for internal use (unit tests)


import subprocess


def test_gpt_class_finetune():
    command = ["python", "part_5/01_main-chapter-code/gpt_class_finetune.py", "--test_mode"]

    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode == 0, f"Script exited with errors: {result.stderr}"
