from unittest import TestCase
from kartinggrid.app_log_utils import log_user_selection
from kartinggrid.app_log_utils import configure_loggers
from logging import getLogger, WARNING, INFO

class MyTestCase(TestCase):
    def setUp(self):
        configure_loggers()
        self.root = getLogger('App')
        self.user = getLogger('App.User')


    def test_root_log_configuration(self):
        self.assertEqual(self.root.level, WARNING)


    def test_user_log_configuration(self):
        self.assertEqual(self.user.level, INFO)


    def test_user_log_contains_info_message(self):
        message = 'Will appear'
        with self.assertLogs(self.user) as cm:
            self.user.info(message)
            self.assertEqual(cm.output, [f'INFO:App.User:{message}'])


    def test_log_user_selection(self):
       message = 'Selected 123'
       with self.assertLogs(self.user) as cm:
           log_user_selection(123)
           self.assertEqual(cm.output, [f'INFO:App.User:{message}'])

    def test_log_result_using_logging_function(self):
        pass

    def test_log_results_using_print(self):
        pass

    def test_log_results_with_decorator_using_logging_function(self):
        pass

    def test_log_results_with_decorator_using_print_function(self):
        pass

if __name__ == '__main__':
    from unittest import main
    main()
