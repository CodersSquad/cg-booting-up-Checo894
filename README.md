[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/swKMSSMl)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16850714&assignment_repo_type=AssignmentRepo)
# Computer Graphics Booting Up

## Let's start with ModernGL

This lab stands to prepare the moderngl development environment. Below the steps and requirements for initial coding tasks. Please make sure to edit the python provided files; for dependencies, you can add the files you need.

1. Install moderngl and its dependencies
2. Make sure that the following programs run
    - [`01_hello_world.py`](./01_hello_world.py)
    - [`06_multiple_objects.py`](./06_multiple_objects.py)
    - [`09_models_and_images.py`](./09_models_and_images.py)
        - _Modify this program to change the box's texture to a correctly aligned TEC logo_
3. Document how to execute the 3 programs in the section below.

* For documentation and missing dependencies, follow these links:
    - https://github.com/moderngl/moderngl
    - https://moderngl.readthedocs.io/

## How to run your program

### Python Installation

As a first requirement, you will need to install Python on your operating system, whichever it is. You can find multiple downloading links for these here>

- [https://www.python.org/downloads/](https://www.python.org/downloads/)

After downloading, be sure to follow all the instructions from the Installing Wizard and then, restarting your PC to succesfully complete the installation and be able to run the Python environment.

### 01_hello_world.py

In order to run this first program, you will need to install the following dependencies:

```
pip install moderngl
pip install pygame
```

Keep in mind that is better to run all this commands in a terminal located in the folder where your this repository is on your PC,
Then you will need to use the following command to run the program:

```
python 01_hello_world.py
```

### 06_multiple_objects.py

In order to run this second program, you will need to install the following dependencies:

```
pip install moderngl
pip install pygame
pip install numpy
pip install PyGLM==2.7.3
```

Keep in mind that is better to run all this commands in a terminal located in the folder where your this repository is on your PC,
Then you will need to use the following command to run the program:

```
python 06_multiple_objects.py
```

### 09_models_and_images.py

In order to run this second program, you will need to install the following dependencies:

```
pip install moderngl
pip install pygame
pip install pillow
pip install PyGLM==2.7.3
pip install pywavefront
```

Keep in mind that is better to run all this commands in a terminal located in the folder where your this repository is on your PC.
Then you will need to use the following command to run the program (this is necesary to be located in the same path that is your program):

```
python 09_models_and_images.py
```

*NOTE: This 'happy path' was created, scripted, tested and ran in a Windows 11 OS environment*

## Grading Policy

- 25% - `01_hello_world.py` is running with no errors
- 25% - `06_multiple_objects.py` is running with no errors
- 25% - `09_models_and_images.py` is running with the requested change (TEC logo texture)
- 25% - Documentation on how to run your programs
