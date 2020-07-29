
import tkinter as tk
from tkinter.filedialog import askopenfiles
from tkinter import Button

class loadedTimingData:
    def __init__(self, data=None):
        self.data = data

    def set_data(self, data):
        self.data = data

if __name__ == '__main__':
    import tkinter as tk
    window = tk.Tk()

    timing_data = TimingData()
    button_settings = dict(parent=window,
                           text="click me",
                           command=lambda : timing_data.set_data(askopenfiles())
    )
    btn=Button(upload_button_settings)
    btn.pack()
    window.mainloop()