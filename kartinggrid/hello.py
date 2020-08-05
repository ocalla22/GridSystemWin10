from tkinter.filedialog import askopenfilenames
from tkinter import Button
from kartinggrid.timing_files import BasicTimingFile
from logging import basicConfig
from logging import info
from functools import wraps

def log_result(func):
    @wraps(func)
    def wrapper():
        original_return_value = func()
        info(original_return_value)
        return original_return_value
    return wrapper

#Decorate askopenfilenames so that it logs user's selection.
askopenfilenames = log_result(askopenfilenames)


def action_on_files(file_names):
        print(len(file_names), 'lol')

def create_upload_button(master, log):
    upload_settings = dict(
        master=master,
        text="add data",
        command=lambda : action_on_files(askopenfilenames())
    )
    return Button(**upload_settings)

def hello():
    print('Jello World')
    return "Hello World"

if __name__ == '__main__':
    import tkinter as tk
    import logging

    basicConfig(level=logging.INFO)
    main_log = logging.getLogger('main')

    window = tk.Tk()
    btf = BasicTimingFile(9)
    upload_button = create_upload_button(window, main_log)
    upload_button.pack()
    window.mainloop()