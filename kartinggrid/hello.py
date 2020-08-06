from tkinter import Button
from tkinter.filedialog import askopenfilenames
import kartinggrid.app_log_utils as alu

# Decorating the askopenfilenames function,
# When called, it operates as normal but additionally the users selection is logged.
askopenfilenames = alu.log_result(func=askopenfilenames,
                                  log_func=alu.log_user_selection)


def action_on_files(file_names):
    print(len(file_names), 'Do stuff with files')


def create_upload_button(master):
    """

    :param master: the Tkinter Widget owning the button
    :return: Tkinter Button Widget that prompts the user to select files
    """
    upload_settings = dict(
        master=master,
        text="add data",
        command=lambda: action_on_files(askopenfilenames())
    )
    return Button(**upload_settings)


def hello():
    print('Jello World')
    return "Hello World"


if __name__ == '__main__':
    import tkinter as tk

    alu.configure_logger()
    window = tk.Tk()
    upload_button = create_upload_button(window)
    upload_button.pack()
    window.mainloop()
