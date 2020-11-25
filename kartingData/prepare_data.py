from pandas import DataFrame

def remove_unnecessary_columns(df:DataFrame):
    '''These columns don't contribute to grid algorithm'''
    columns_to_drop = ['#', 'Lead', 'Spd', 'Hits',
                       'Strength', 'Noise', 'Transponder',
                       'Backup Tx', 'Class', 'Photocell Time',
                       'Elapsed Tm', 'Passing Tm', 'Backup Passing Tm',
                       'RaceEvent']
    return df.drop(columns=columns_to_drop)


def cast_driver_number_and_laps_to_int(df:DataFrame):
    return df.astype({'No.': 'int16', 'Laps': 'int16'})


def remove_deleted_rows_and_deleted_column(df:DataFrame):
    '''race overseer marked these to be deleted.'''
    deleted_rows = df.index[df['Deleted'] != 'No']
    return (df.drop(labels=deleted_rows).drop(columns='Deleted'))


def remove_zeroth_and_first_laps(df:DataFrame):
    '''#Laps 0,1 don't have timing data'''
    laps_0_1_rows = df.index[df['Laps'] < 2]
    return df.drop(labels=laps_0_1_rows)


def prepare_dataframe(df:DataFrame):
    '''#pipe the above utilities together to prepare raw data.'''
    prepped_data = (df
                    # minimise memory footprint
                    .pipe(remove_unnecessary_columns)
                    # data marked as deleted by Overseer
                    .pipe(remove_deleted_rows_and_deleted_column)
                    # easier on the eyes and memory.
                    .pipe(cast_driver_number_and_laps_to_int)
                    # these don't have timing data? Funny business rule here?
                    .pipe(remove_zeroth_and_first_laps)
                    )
    return prepped_data
