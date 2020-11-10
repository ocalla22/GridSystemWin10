import pandas as pd
from os.path import join, dirname


def _build_dataframe_from(HTMLfile):
    package = dirname(__file__)
    path = join(package, 'data', HTMLfile)
    return pd.read_html(path, flavor='html5lib')[0]

def load_heat1():
    return _build_dataframe_from('Bambino - Heat 1.html')

def load_heat2():
    return _build_dataframe_from('Bambino - Heat 2.html')

def load_final():
    return _build_dataframe_from('Bambino - Final.html')

def load_qualification():
    return _build_dataframe_from('Bambino - Qualification.html')