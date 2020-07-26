# GridSystem
A Standalone Application that can be run on windows 10, that ingests timing infromation and outputs the racing grid formation for an event.
It should save the gridman from manually computing the grid by hand from timing data and letting him safely store the grid format.

This document will give step by step instructions to pull the project, setup a virtual environment and package the application using pyinstaller. 
This repository purpose to bundle the application to make a standalone .exe file the for GridSystem app with Python3.7 and TKinter.

Currently MacOS is not supported due to complexities with bundling Tcl and TK using PyInstaller, but its unlikely the target market use MacOS. As per the following [issue](https://github.com/pyinstaller/pyinstaller/issues/3753) and other related issues.

## Assumptions
Made to be beginner friendly, but a few basic assumptions are made.
1. python3.7 has been installed and can be ran from CLI with the python command. Depending on your local configuration you may need the python3 command instead.
2. PIP3 is installed for your Python distribution and can be called with pip command. Depending on your setup you may need to call PIP3 command instead.
3. Familiarity with Git.
4. Useing Git Bash on Windows CLI. WSL won't work as it doesn't have a GUI yet.

## Background

### What's a Standalone Application
A [Standalone-Application](https://medium.com/swlh/a-guide-to-standalone-applications-and-why-enterprises-need-them-1764fd1f8a0c) is used so that once the application is distributed, it should work out-of-the-box, for Windows10. This is convinient for non-developers as they don't need to setup environments or install dependencies. Everything the application needs to run is bundled and contained within it.

The assumption is that the user can input manually curated timing data documents in a known format then this application. The grid man can update the formation on the fly to make any adjustment last minute and these are recorded. There is no reliance on network connections.

### What's a Virtual Environment
Virtual environments are a way of creating an isolated space in your system. It helps keep the applications dependencies out of your base system and keeping any system dependencies from interfereing with the application. The "right way" to use a virtual environment was adopted form [here](https://medium.com/@jtpaasch/the-right-way-to-use-virtual-environments-1bc255a0cba7). There are a few tools that can be used for this, but venv will be used as its native to python3.3+.

## Quickstart - Build Application the Easy Way
Use this way if you just want to produce the executable the way its been delivered today.
This script is the easy way to setup the virtual environment, install requirements and build the standalone application. Simply clone the repository, enter it and run the build.sh script.

```bash
git clone https://github.com/ocalla22/GridSystemWin10.git
cd GridSystemWin10
./scripts/build.sh
```

The dist folder contains the hello.exe file that can be distribute in order to run the standalone application. This will only work for windows systems.

```bash
./dist/hello/hello.exe
```

## Long Way - Manually Execute Build Steps
If you want to modify the code or use different environments you should use this way.

### Pull Project
Navigate to the directory using CLI in which you intend to store the project. For the purposes of this document, it will be assumed its contained in this directory. ~/MyProjects.

Pull/Clone this repository and move into its directory.
```bash
cd ~/MyProjects
git clone https://github.com/ocalla22/GridSystemWin10.git
cd GridSystemWin10
```

### Setup Virtual Environment
As per [The recomended way of using a virtual environment](https://medium.com/@jtpaasch/the-right-way-to-use-virtual-environments-1bc255a0cba7), now that you're in the GridSystemWin10 directory, create a virtual environment. Run Python's builtin venv module to create a new virtual environment called "myvenv". Next, install any dependencies listed in development listed in requirements.txt 
- Note : the virtual environment that is created will use the version of python that corresponds the vertion of the Python command used to invoke it. 
- For example, if the command "Python" points to version A, and "Python3" points to version B and the command executed is Python3 -m venv myvenv, will create a virtual environment named "myvenv" which uses version B of Python. 

Create the virtual environment, activate it and install development requirements.
```bash
python3 -m venv myvenv 
source myvenv/Scripts/activate
pip3 install -r requirements.txt
```

If you need to deactivate the virtual environment you can use the deactivate command. Remember to reactivate it again when you come back to the project, using the activate script. No need to install requirements, or create a new venv

```bash
deactivate

source myvenv/Scripts/activate
```

### Package the Standalone Application
Run pyinstaller on the main application file. This will create the .spec file, and a build and dist folder. Again, source control will ignore these as they are in the .gitignore file.

```bash
pyinstaller ./kartinggrids/hello.py
```

The dist folder the hello.exe file that can be distribute in order to run the standalone application. This will only work for windows systems only.

```bash
./dist/hello/hello.exe
```

## What about Mac OS?
You can test the application on MacOS by setting up the environment and running the main file. You don't need to run pyinstaller. Again this application hasn't been packaged into a standalone application, it has system dependencies. User's (non-developers) would need to have python3 installed, and a wizard would have to be made to install if for them.
```bash
python3 ./kartinggrid/hello.py
```

## Packaging with PIP
For no particular reason, put this on PyPI, so the kartingGrids package can be accessed.
You can pull the project (see above), and install twine to help package this up nicely.

```bash
python3 setup.py bdist_wheel
python -m twine upload dist/*
```

then this can be pulled using 

```bash
pip3 install GridSystemWin10
python3
```
Then from your interpreter session

```python
from kartinggrids import hello
hello.hello()
hello world
```

If you don't have one alreayd you'll need a .pypirc folder in your home directory.

```
[distutils] 
index-servers=pypi
[pypi] 
repository = https://upload.pypi.org/legacy/ 
username =ocalla22
```
