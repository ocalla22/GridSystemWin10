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


def action_on_user_selected_files():
    return action_on_files(_askopenfilenames())


def get_upload_button_settings():
    return dict(
        text="add data",
        command=action_on_user_selected_files
    )


if __name__ == '__main__':
    import tkinter as tk
    alu.configure_loggers()
    window = tk.Tk()
    upload_button = Button(master=window, **get_upload_button_settings())
    upload_button.pack()
    window.mainloop()
