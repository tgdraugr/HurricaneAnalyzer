import unittest
import hurricane_analyzer


class MyTestCase(unittest.TestCase):
    def test_analyzer_call(self):
        self.assertEqual(hurricane_analyzer.works(), True)


if __name__ == '__main__':
    unittest.main()
