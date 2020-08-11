import io
from logging import getLogger, WARNING, INFO
from kartinggrid.app_log_utils import log_user_selection, configure_loggers, log_result_with
from kartinggrid.TKinterTestCase import TKinterTestCase
from unittest import TestCase
from unittest.mock import patch



class TestAppLogUtils(TKinterTestCase):
    def setUp(self):
        super().setUp()
        configure_loggers()
        self.app_logger = getLogger('App')
        self.user = getLogger('App.User')
        self._greeting = lambda name : f'Hello {name}' #just a simple function ot test with

    def test_root_log_configuration(self):
        self.assertEqual(self.app_logger.level, WARNING)


    def test_user_log_configuration(self):
        self.assertEqual(self.user.level, INFO)


    def test_user_log_contains_info_message(self):
        message = 'Will appear'
        with self.assertLogs(self.user) as log_tester:
            self.user.info(message)
            self.assertEqual(log_tester.output, [f'INFO:App.User:{message}'])


    def test_log_user_selection(self):
       message = 'Selected 123'
       with self.assertLogs(self.user) as log_tester:
           log_user_selection(123)
           self.assertEqual(log_tester.output, [f'INFO:App.User:{message}'])


    def test_log_results_with_decorator_using_logging_function(self):
        @log_result_with(self.user.info)
        def decorated_function(x):
            return self._greeting(x)
        with self.assertLogs(self.user) as log_tester:
            func_output = decorated_function('Monty')
            self.assertEqual(log_tester.output, [f'INFO:App.User:{func_output}'])


    @patch('sys.stdout', new_callable=io.StringIO)
    def test_log_results_with_decorator_using_print_function(self, mock_stdout):

        @log_result_with(print)
        def decorated_function(x):
            return self._greeting(x)

        func_output = decorated_function('Monty')
        self.assertEqual(mock_stdout.getvalue(), f'{func_output}\n')



if __name__ == '__main__':
    from unittest import main
    main()
