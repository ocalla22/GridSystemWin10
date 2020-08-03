from tkinter.filedialog import askopenfiles
from tkinter import Button
from kartinggrid.timing_files import BasicTimingFile


def log_contents_of(files):
    for file in files:
        for line in file:
            print(line)

def update_files():
    files = askopenfiles()
    log_contents_of(files)

def pack_button(master):
    upload_settings = dict(
        master=master,
        text="add data",
        command=lambda: update_files()
    )
    Button(**upload_settings).pack()


if __name__ == '__main__':
    import tkinter as tk
    window = tk.Tk()
    btf = BasicTimingFile(9)
    print(btf.data)

    pack_button(window)
    window.mainloop()