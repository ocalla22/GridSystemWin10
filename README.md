# GridSystem
A Standalone Application that can be run on windows 10, that ingests timing infromation and outputs the correct racing Grid Formation for an event.
It should save the gridman from manually computing the grid by hand from timing data.

Running with Python36 currently.

## Pull Project
```bash
git clone https://github.com/ocalla22/GridSystem.git
```

## Setup a virtual environment
A virtual environment can be used, it'll be reffered to as myvenv. Use pyvenv or virtualenv. We'll use virtualenv for this example.

```bash
pip install virtualenv
virtualenv myvenv```

For Windows
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
