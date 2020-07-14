from unittest import TestCase 
from hello import hello

class TestHello(TestCase):

    def test_hello(self):
        self.assertEqual(hello(), "Hello World")

if __name__ == "__main__":
    from unittest import main
    main()
