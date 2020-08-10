from tkinter import Button
import tkinter.filedialog as fd
import kartinggrid.app_log_utils as alu


# Decorating this function; it works as usual with the additional behaviour of logging the return value.
@alu.log_result_with(alu.log_user_selection)
def _askopenfilenames():
    return fd.askopenfilenames()


def action_on_files(file_names):
    #Do stuff with files
    return len(file_names)


def create_upload_button(master):
    """

    :param master: the Tkinter Widget owning the button
    :return: Tkinter Button Widget that prompts the user to select files
    """
    upload_settings = dict(
        master=master,
        text="add data",
        command=lambda : action_on_files(_askopenfilenames())
    )
    return Button(**upload_settings)


if __name__ == '__main__':
    import tkinter as tk
    alu.configure_loggers()
    window = tk.Tk()
    upload_button = create_upload_button(window)
    upload_button.pack()
    window.mainloop()
