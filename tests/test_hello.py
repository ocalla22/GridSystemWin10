import io
import kartinggrid.hello as h
import tkinter
import tkinter.filedialog
from unittest import TestCase, skip
from unittest.mock import patch

class TestHello(TestCase):

    def setUp(self):
        self.master = tkinter.Tk()


    def test_create_upload_buttons_configuration_except_command(self):
        button = h.create_upload_button(self.master)
        self.assertEqual(button.master, self.master)
        self.assertEqual(button['text'], "add data")


    @patch('tkinter.filedialog.askopenfilenames', return_value='Heddo World')
    def test_button_invokes_action_on_user_selected_files(self, patched_function):
        button = h.create_upload_button(self.master)
        self.assertEqual(button.invoke(), len("Heddo World"))
        self.assertEqual(patched_function.call_count, 1)
        #Test action_on_files is called with mocked parm of user input.

    def test_action_on_files(self):
        #test the action and side effects etc.
        pass


if __name__ == "__main__":
    from unittest import main
    main()
