# Setup Instructions

This document lists different approaches for setting up your machine and using the code in this repository. I recommend browsing through the different sections from top to bottom and then deciding which approach best suits your needs.

## Quickstart

If you already have a Python installation on your machine, the quickest way to get started is to install the package requirements from the [../requirements.txt](../requirements.txt) file by executing the following pip installation command from the root directory of this code repository:

```bash
pip install -r requirements.txt
```
# Local Setup

This section provides recommendations for running the code in this course locally. Note that the code in repository is designed to run on conventional laptops within a reasonable timeframe and does not require specialized hardware. I tested all code on an M2 MacBook Pro Max laptop with 32 GB RAM. Additionally, if your laptop or desktop computer has an NVIDIA GPU, the code will automatically take advantage of it.

## Setting up Python

If you don't have Python set up on your machine yet, I have written about my personal Python setup preferences in the following directories:

- [01_optional-python-setup-preferences](./01_optional-python-setup-preferences)
- [02_installing-python-libraries](./02_installing-python-libraries)

## Visual Studio Code Editor

There are many good options for code editors. My preferred choice is the popular open-source [Visual Studio Code (VSCode)](https://code.visualstudio.com) editor, which can be easily enhanced with many useful plugins and extensions (see the *VSCode Extensions* section below for more information). Download instructions for macOS, Linux, and Windows can be found on the [main VSCode website](https://code.visualstudio.com).

&nbsp;

## VSCode Extensions

If you are using Visual Studio Code (VSCode) as your primary code editor, you can find recommended extensions in the `.vscode` subfolder. These extensions provide enhanced functionality and tools helpful for this repositoy.

To install these, open this "setup" folder in VSCode (File -> Open Folder...) and then click the "Install" button in the pop-up menu on the lower right.

Alternatively, you can move the `.vscode` extension folder into the root directory of this GitHub repository:

```bash
mv setup/.vscode ./
```

Then, VSCode automatically checks if the recommended extensions are already installed on your system every time you open the `Building-an-LLM-From-Scratch` main folder.

&nbsp;

# Cloud Resources

This section describes cloud alternatives for running the code presented in this course.

While the code can run on conventional laptops and desktop computers without a dedicated GPU, cloud platforms with NVIDIA GPUs can substantially improve the runtime of the code, especially in parts 4 to 6.

&nbsp;

## Using Lightning Studio

For a smooth development experience in the cloud, I recommend the [Lightning AI Studio](https://lightning.ai/) platform, which allows users to set up a persistent environment and use both VSCode and Jupyter Lab on cloud CPUs and GPUs.

Once you start a new Studio, you can open the terminal and execute the following setup steps to clone the repository and install the dependencies:

```bash
git clone https://github.com/Sangwan70/Building-an-LLM-From-Scratch.git
cd Building-an-LLM-From-Scratch
pip install -r requirements.txt
```

Then, navigate to the Python script or Jupyter Notebook you want to run. Optionally, you can also easily connect a GPU to accelerate the code's runtime, for example, when you are pretraining the LLM in part 4 or finetuning it in part 5 and 6.

&nbsp;

# Questions?

If you have any questions, please don't hesitate to reach out via the [Discussions](https://github.com/Sangwan70/Building-an-LLM-From-Scratch/discussions) forum in this GitHub repository.
