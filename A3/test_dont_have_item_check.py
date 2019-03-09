from unittest import TestCase
from sud import dont_have_item_check
from unittest.mock import patch
import io
import character
import map


class TestDont_Have_item_check(TestCase):

    def test_have_bread(self):
        character.character_info['inventory'] = []
        character.character_info['inventory'] = ['bread']
        self.assertFalse(dont_have_item_check('use bread'))

    def test_have_sword(self):
        character.character_info['inventory'] = []
        character.character_info['inventory'] = ['sword']
        self.assertFalse(dont_have_item_check('use sword'))

    def test_dont_have_item(self):
        character.character_info['inventory'] = []
        self.assertTrue(dont_have_item_check('bread'))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_dont_have_item_message(self, mock_output):
        character.character_info['inventory'] = []
        dont_have_item_check('bread')
        expected_output = 'You dont have that item\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

