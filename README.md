# Simple-Project-Py
Below are the steps in order to get started building a python project, by presenting the step-by-step process to recreate this project from scratch.


## Prerequisites
Having the `conda` command available on your system. This is obtained by installing one (and only one!) of the following:
- Anaconda
- Miniconda
- Condaforge
- Miniforge


## Create & Clone a Github repository
In Github, create a new reprository `<repo-name>`. It is advised to start the new repo with a `README` and with a `.gitignore` taylored for python.

In your local laptop, open a conda shell, and move to a directory where you want to store your project
```shell
cd path/to/parent/directory
```
If your path contains spaces, enclose the path into `" "`.

Git clone your remote repository to your local directory
```shell
git clone https://github.com/<user-name>/<repo-name>.git
```

Move into this newly created directory
```shell
cd path/to/parent/directory/<repo-name>
```


## Initialize a virtual environment with `conda`
Create a new `environment.yaml` file with content (here we used `<env-name> = simple-project-py`).
```shell
name: <env-name>
channels:
	- defaults
dependencies:
	- python=3.11.9
	- pip=24.2
	- pip:
	- poetry==1.8.3
```
Create a new conda environment out of this file
```shell
conda env create -f environment.yaml
```
Activate this newly created environment
```shell
conda activate <env-name>
```


## Initialize your dependencies with `poetry`
Create a new dependency manifest
```shell
poetry init
```
Validate the default values. When asked to manage dependencies interactively, type `no`.

Install `jupyter`, `fire` and `streamlit` dependencies
```shell
poetry add fire streamlit
poetry add -G dev jupyter
```
See poetry's documentation on how to install a specific version of a dependency, or to define an allowed range of versions.


## Install your project in editable mode
Create a folder `src/<mypkgname>` in your project (here we used `<mypkgname> = simplepypkg`).

In this folder, create a python file named `__init__.py` and leave it empty.

Open your `pyproject.toml` file, look at the section `[tool.poetry]` of your file and add an extra line
```shell
packages = [{include = "<mypkgname>", from = "src"}]
```
Run
```shell
poetry install
```


## Add source code to your project
A python project's source code carry the main utility functions of your project, such as data loaders, preprocessing, training and evaluation of a Machine Learning model. This is illustrated with the minimalistic example below.

Create a new python module `src/<mypkgname>/custom_functions.py` with content
```python
def is_odd(n: int) -> bool:
    '''
    Assert whether a given integer is odd.
    '''
    return bool(n % 2)


def is_even(n: int) -> bool:
    '''
    Assert whether a given integer is even.
    '''
    return not is_odd(n)
```
You can use this code in a Jupyter notebook or in a python interpreter
```python
from <mypkgname>.custom_functions import is_even, is_odd

is_even(12345)
is_odd(12345)
```


## Create an entry point of your project
An entry point is a script that provides the functionality desired from this project. To that end wer will use the `fire` package that seamessly converts command line arguments into inputs of python functions.

Create a `cli_demo.py` python module at the root of your project, and add content
```python
from fire import Fire

from <mypkgname>.custom_functions import is_even


if __name__ == '__main__':
	Fire(is_even)
```

You can now check is an integer (say `12345`) is even by running in a command line interface located at your repository folder and with your conda environment activated
```shell
python -m cli_demo 12345
```
The argument `12345` was handled and converted into input for the `is_even` python function.


## Create a demo app
Create a `app_demo.py` pythyon module at the root of your project, and add content
```python
import streamlit as st

from simplepypkg.custom_functions import is_even


def app():
    st.header('Test if your number is Even 💚')
    n = st.slider('Provide an integer to test', min_value = 0, max_value = 100)
    if n:
        resp = is_even(n)
        if resp:
            st.success(f'{n} is even !')
        else:
            st.info(f'{n} is odd...')


if __name__ == '__main__':
	app()
```

You can now launch a nice looking app by running in a command line interface located at your repository folder and with your conda environment activated
```shell
streamlit run app_demo.py
```


## Push your modifications to github
Stage your local changes
```shell
git add .
```
Commit these changes to your local git history
```shell
git commit
```
Push these commited changes towards your remote Github repository
```shell
git push
```
You should be able to see the changes in your Github repository by refreshing the web page `https://github.com/<git-user-name>/<repo-name>`.


## Congratulations ! 
You made it to the end of this tutorial. Happy coding !
