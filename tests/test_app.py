import kartinggrid.app as main
from unittest import TestCase
from unittest.mock import patch

class TestHello(TestCase):


    def test_get_upload_button_settings(self):
        expected = dict(
            text="add data",
            command=main.action_on_user_selected_files
        )
        self.assertDictEqual(main.get_upload_button_settings(), expected)


    def test_action_on_files(self):
        self.assertEqual(main.action_on_files('Hello World'), len('Hello World'))
        #test the action and side effects etc.
        pass


    @patch('tkinter.filedialog.askopenfilenames', return_value='Heddo World')
    def test_action_on_user_selected_files(self, patched_function):
        self.assertEqual(main.action_on_user_selected_files(), len("Heddo World"))
        self.assertEqual(patched_function.call_count, 1)
        # Test action_on_files is called with mocked parm of user input.


if __name__ == "__main__":
    from unittest import main
    main()
