from tkinter.filedialog import askopenfiles
from tkinter import Button
from kartinggrid.timing_files import BasicTimingFile


def log_contents_of(file):
    for line in file:
        print(line)

def log_user_selection(files):
    for file in files:
        log_contents_of(file)

def user_selects_files():
    files = askopenfiles()
    log_user_selection(files)

def create_upload_button(master):
    upload_settings = dict(
        master=master,
        text="add data",
        command=user_selects_files
    )
    return Button(**upload_settings)

def hello():
    print('Jello World')
    return "Hello World"

if __name__ == '__main__':
    import tkinter as tk
    window = tk.Tk()
    btf = BasicTimingFile(9)
    upload_button = create_upload_button(window)
    upload_button.pack()
    window.mainloop()