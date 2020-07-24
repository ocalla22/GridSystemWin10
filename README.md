# GridSystem
A Standalone Application that can be run on windows 10, that ingests timing infromation and outputs the correct racing grid formation for an event.
It should save the gridman from manually computing the grid by hand from timing data.

This Repo is for bundling the application to make a standalone .exe file the for GridSystem app with Python3.8 and TKinter.

Currently MacOS is not supported in this Repo due to complexities with bundling Tcl and TK using PyInstaller, but its unlikely the target market use MacOS. As per this, and related [issues](https://github.com/pyinstaller/pyinstaller/issues/3753)

A [Standalone-Application](https://medium.com/swlh/a-guide-to-standalone-applications-and-why-enterprises-need-them-1764fd1f8a0c) is used so that once the application is distributed, it should work out of the box with Windows10. This is particularly convinient for non-developers as they don't need to setup environments or install dependencies. Everything the application needs to run is bundled and contained within it.

The assumption is that the user can input manually curated timing data documents in a known format then this application. The grid man can update the formation on the fly to make any adjustment last minute and these are recorded. There is no reliance on network connections.

This document will give step by step instructions on how to pull the project, setup a virtual environment package the application using pyinstaller. 
It assumes that you already have Python and are familiar with Git. When running commands the assumption is that you are using bash either with Git Bash or WSL.

A virtual environment will be used to keep your own system seperate from the project's environment, this will stop your systems environment from colliding with the application and similarly keep the applications dependencies out of your system. The recomended setup was adopted from [here](https://medium.com/@jtpaasch/the-right-way-to-use-virtual-environments-1bc255a0cba7)

## Pull Project + Setup Virtual Environment and Dependencies.
1. Pull/Clone the Repo
```bash
git clone https://github.com/ocalla22/GridSystemWin10.git
```

2. Setup Virtual Environment
The recomended way of setting up a virtual environment as noted above is that you go into the project folder, within the GridSystem directory.
There are a few tools built for this, but we will use venv as its native to pthon3.3+.

. Use pyvenv or virtualenv. This will stop you pulling needless dependencies and packages into your system.

```bash
pip install virtualenv
virtualenv myvenv
```
For Bash Windows
source myvenv/Scripts/activate

For MacOS
source myvenv/bin/activate

in both systems we can deactivate the venv using the deactivate command
deactivate

install pyinstaller, we're using pyinstaller3.6 this makes packaging and generating the standalone executable easy.

pip install pyinstaller==3.6

install twine, we'll use that for uploading kartinggrids to pip and making it a module that can be pulled.

pip install twine

## Package the Standalone Application
This won't work on MacOS. Pyinstaller, Tkinter and MacOS tend to disagree. For this reason its not so straight forward to make a standalone tkinter app for MacOS. Luckily the target market here is Windows users.
So the following instructions assume you've downloaded the project on Windows OS.

Run pyinstaller on the main application file. This will create the .spec file, and a build and dist folder. In the dist folder the .exe file to run the standalone application.
pyinstaller ./kartinggrids/hello.py

you can run find the standalone executable. Or distribute it for windows systems.
./dist/hello/hello.exe

You can test the application on MacOS by setting up the environment and running the main file.
./kartinggrid/hello.py, that should be enough to enhancement, but i strongly encourage packaging on windows only.


## Packaging with PIP
On a high level we need to build a distributable and push it up to a remote pypi (python package index) repository.

First create the distributable

python setup.py bdist_wheel

and upload to pypi, assuming you have a .pypirc folder setup in your home.

[distutils] 
index-servers=pypi
[pypi] 
repository = https://upload.pypi.org/legacy/ 
username =ocalla22

python -m twine upload dist/*
