import numpy as np
from pandas import DataFrame

#Star Wars Name Generator
from swnamer import NameGenerator

def _extract_race_event_column(df:DataFrame):
    '''RaceEvent extracted from Name column'''
    return df.assign(RaceEvent=np.where(df['No.'].notnull(), '', df['Name']))

def _extract_novice_column_from_name(df:DataFrame):
    '''if name has '(N) in it.'''
    return df.assign(Novice=df.Name.apply(lambda x : '(N)' in x))

def _get_sw_nickname(seed=None):
    return NameGenerator(use_characters=True,
                         use_species=False,
                         use_planets=False,
                         lowercase=True,
                         separator='_',
                         seed=seed)\
        .generate()

def _use_star_wars_nicknames(df:DataFrame):
    '''if there's a driver number, map it to StarWars nickname'''
    return df.assign(Name=np.where(df['No.'].notnull(), df['No.'].apply(_get_sw_nickname), ''))

def do_preprocessing(df:DataFrame):
    '''Extract info in Name field before overriding it to SW nickname'''
    preprocessed_data = (df
                         .pipe(_extract_novice_column_from_name)
                         .pipe(_extract_race_event_column)
                         .pipe(_use_star_wars_nicknames)
                         )
    return preprocessed_data
