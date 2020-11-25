import pandas as pd
from os.path import join, dirname
from kartingData.preprocessing import do_preprocessing

def _build_preprocessed_dataframe_from(HTMLfile:str):
    package = dirname(__file__)
    path = join(package, 'data', HTMLfile)
    df = pd.read_html(path, flavor='html5lib')[0]
    return df.pipe(do_preprocessing)

def load_heat1():
    return _build_preprocessed_dataframe_from('Bambino - Heat 1.html')

def load_heat2():
    return _build_preprocessed_dataframe_from('Bambino - Heat 2.html')

def load_final():
    return _build_preprocessed_dataframe_from('Bambino - Final.html')

def load_qualification():
    return _build_preprocessed_dataframe_from('Bambino - Qualification.html')
