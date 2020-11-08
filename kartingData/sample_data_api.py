import pandas as pd
from os import getcwd, path


def _build_dataframe_from(HTMLfile):
    path_to_file = path.join(getcwd(), 'data', HTMLfile)
    return pd.read_html(path_to_file, flavor='html5lib')


def load_heat1():
    return _build_dataframe_from('Bambino - Heat 1.html')


def load_heat2():
    return _build_dataframe_from('Bambino - Heat 2.html')


def load_final():
    return _build_dataframe_from('Bambino - Final.html')


def load_qualification():
    return _build_dataframe_from('Bambino - Qualification.html')
