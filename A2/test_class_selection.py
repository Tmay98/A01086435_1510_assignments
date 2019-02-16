from unittest import TestCase
from unittest.mock import patch
import io
from dungeonsanddragons import class_selection


class TestClass_selection(TestCase):

    @patch('builtins.input', side_effect=['barbarian'])
    def test_correct_class_selection(self, mock_input):
        self.assertTrue(class_selection() == 'barbarian')

    @patch('builtins.input', side_effect=['SoRceRER'])
    def test_capital_letters(self, mock_input):
        self.assertTrue(class_selection() == 'sorcerer')

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['jfg54g', 'wizard'])
    def test_incorrect_input(self, mock_input, mock_stdout):
        expected_output = 'You did not enter a correct class, try again\n'
        class_selection()
        output = mock_stdout.getvalue()
        self.assertEqual(output, expected_output)
