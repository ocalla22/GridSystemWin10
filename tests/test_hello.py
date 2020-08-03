from unittest import TestCase
import kartinggrid.hello
import io
from unittest.mock import patch

class TestHello(TestCase):


    @patch('kartinggrid.hello.hello', return_value='Heddo World')
    def test_hello_further(self, patched_function):
        self.assertEqual(kartinggrid.hello.hello(), "Heddo World")
        self.assertTrue(patched_function.called)
        self.assertEqual(patched_function.call_count, 1)


    @patch('sys.stdout', new_callable=io.StringIO)
    def test_yet_another_hello(self, mock_stdout):
        kartinggrid.hello.hello()
        self.assertEqual(mock_stdout.getvalue(), 'Jello World\n')


if __name__ == "__main__":
    from unittest import main
    main()
