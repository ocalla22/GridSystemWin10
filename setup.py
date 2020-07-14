from os import path
from setuptools import find_packages

def get_readme_path():
    readme_filename = "README.md"
    return path.join(path.dirname(__file__), readme_filename )

def get_readme():
    return open(get_readme_path()).read()   

SETUP_ARGS = dict(
    name = 'GridSystem',
    version = 1,
    description = "to make the grid mans job easy",
    long_description = get_readme(),
    url = "https://github.com/ocalla22/GridSystem",
    author = "Andy OC",
    author_email = "Not for you",
    license = "MIT",
    include_package_data = True,
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        ],
    packages = find_packages(),
    py_modules = ['hello'],
    install_requires = [],
    )
    
if __name__ == "__main__":
    from setuptools import setup
    setup(**SETUP_ARGS)
