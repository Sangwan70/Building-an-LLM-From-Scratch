# Python Setup


There are several ways you can install Python and set up your computing environment.

(I am using computers running MacOS, but this workflow is similar for Linux machines and may work for other operating systems as well.)

<br>

## 1. Download and install Miniforge

Download miniforge from the GitHub repository [here](https://github.com/conda-forge/miniforge).

<img src="https://raw.githubusercontent.com/Sangwan70/Building-an-LLM-From-Scratch/refs/heads/main/setup/images/download.webp" alt="download" width="700px">

Depending on your operating system, this should download either an `.sh` (macOS, Linux) or `.exe` file (Windows).

For the `.sh` file, open your command line terminal and execute the following command

```bash
sh ~/Desktop/Miniforge3-MacOSX-arm64.sh
```

where `Desktop/` is the folder where the Miniforge installer was downloaded to. On your computer, you may have to replace it with `Downloads/`.

<img src="https://raw.githubusercontent.com/Sangwan70/Building-an-LLM-From-Scratch/refs/heads/main/setup/images/miniforge-install.webp" alt="miniforge-install" width="700px">

Next, step through the download instructions, confirming with "Enter".

<br>

## 2. Create a new virtual environment

After the installation was successfully completed, I recommend creating a new virtual environment called `LLMs`, which you can do by executing

```bash
conda create -n LLMs python=3.12
```

> Many scientific computing libraries do not immediately support the newest version of Python. Therefore, when installing PyTorch, it's advisable to use a version of Python that is one or two releases older. For instance, if the latest version of Python is 3.13, using Python 3.11 or 3.12 is recommended.

Next, activate your new virtual environment (you have to do it every time you open a new terminal window or tab):

```bash
conda activate LLMs
```

<img src="https://raw.githubusercontent.com/Sangwan70/Building-an-LLM-From-Scratch/refs/heads/main/setup/images/activate-env.webp" alt="activate-env" width="600px">

<br>

## 3. Install new Python libraries


To install new Python libraries, you can now use the `conda` package installer. For example, you can install [JupyterLab](https://jupyter.org/install) as follows:

```bash
conda install jupyterlab
```

You can also still use `pip` to install libraries. By default, `pip` should be linked to your new `LLms` conda environment:

<img src="https://raw.githubusercontent.com/Sangwan70/Building-an-LLM-From-Scratch/refs/heads/main/setup/images/check-pip.webp" alt="check-pip" width="600px">

<br>

## 4. Install PyTorch

PyTorch can be installed just like any other Python library or package using pip. For example:

```bash
pip install torch
```

However, since PyTorch is a comprehensive library featuring CPU- and GPU-compatible codes, the installation may require additional settings and explanation.

It's also highly recommended to consult the installation guide menu on the official PyTorch website at [https://pytorch.org](https://pytorch.org).

<img src="https://raw.githubusercontent.com/Sangwan70/Building-an-LLM-From-Scratch/refs/heads/main/setup/images/pytorch-installer.webp" width="600px">


## 5. Installing Python packages and libraries used in this course

Please refer to the [Installing Python packages and libraries used in this course](../02_installing-python-libraries/README.md) document for instructions on how to install the required libraries.

<br>

---


Any questions? Please feel free to reach out in the [Discussion Forum](https://github.com/Sangwan70/Building-an-LLM-From-Scratch/discussions).
