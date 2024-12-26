# Installing Python Packages and Libraries Used In This Book

This document provides more information on double-checking your installed Python version and packages. (Please see the [../01_optional-python-setup-preferences](../01_optional-python-setup-preferences) folder for more information on installing Python and Python packages.)

I used the following libraries listed [here](https://github.com/Sangwan70/Building-an-LLM-From-Scratch/blob/main/requirements.txt) for this course. Newer versions of these libraries are likely compatible as well. However, if you experience any problems with the code, you can try these library versions as a fallback.

To install these requirements most conveniently, you can use the `requirements.txt` file in the root directory for this code repository and execute the following command:

```bash
pip install -r requirements.txt
```

Alternatively, you can install it via the GitHub URL as follows:

```bash
pip install -r https://raw.githubusercontent.com/Sangwan70/Building-an-LLM-From-Scratch/refs/heads/main/requirements.txt
```


Then, after completing the installation, please check if all the packages are installed and are up to date using

```bash
python python_environment_check.py
```

<img src="https://raw.githubusercontent.com/Sangwan70/Building-an-LLM-From-Scratch/refs/heads/main/setup/images/check_1.webp" width="600px">

It's also recommended to check the versions in JupyterLab by running the `python_environment_check.ipynb` in this directory, which should ideally give you the same results as above.

<img src="https://raw.githubusercontent.com/Sangwan70/Building-an-LLM-From-Scratch/refs/heads/main/setup/images/check_2.webp" width="500px">

If you see the following issues, it's likely that your JupyterLab instance is connected to wrong conda environment:

<img src="https://raw.githubusercontent.com/Sangwan70/Building-an-LLM-From-Scratch/refs/heads/main/setup/images/jupyter-issues.webp" width="450px">


<br>


## Installing PyTorch

PyTorch can be installed just like any other Python library or package using pip. For example:

```bash
pip install torch
```

However, since PyTorch is a comprehensive library featuring CPU- and GPU-compatible codes, the installation may require additional settings and explanation.

It's also highly recommended to consult the installation guide menu on the official PyTorch website at [https://pytorch.org](https://pytorch.org).

<img src="https://raw.githubusercontent.com/Sangwan70/Building-an-LLM-From-Scratch/refs/heads/main/setup/images/pytorch-installer.webp" width="600px">

<br>

---




Any questions? Please feel free to reach out in the [Discussion Forum](https://github.com/Sangwan70/Building-an-LLM-From-Scratch/discussions).
