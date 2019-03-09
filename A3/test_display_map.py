from unittest import TestCase
import map
import character
from map import display_map
from unittest.mock import patch
import io


class TestDisplay_map(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_displays_3x3_portion(self, mock_output):
        display_map()
        expected_output = ' | ------\n\n' \
                          ' |  P    \n\n' \
                          ' \ ------\n\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

