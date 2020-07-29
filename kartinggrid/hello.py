
import tkinter as tk
from tkinter import filedialog

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

def hello():
    return "Hello World"

if __name__ == '__main__':
    import tkinter as tk
    window = tk.Tk()
    button = tk.Button(window, text='Open', command=UploadAction)
    button.pack()
    label = tk.Label(text=hello())
    label.pack()
    window.mainloop()
