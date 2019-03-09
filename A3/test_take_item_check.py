from unittest import TestCase
from sud import take_item_check
import io
from unittest.mock import patch
import character
import map


class TestTake_item_check(TestCase):

    def test_take_key(self):
        character.character_info['inventory'] = []
        character.set_column(5)
        character.set_row(5)
        map.set_map(5, 5, ' K ')
        take_item_check('take key')
        self.assertEqual(character.get_character_info()['inventory'], ['key'])

    def test_take_sword(self):
        character.character_info['inventory'] = []
        character.set_column(5)
        character.set_row(5)
        map.set_map(5, 5, ' S ')
        take_item_check('take sword')
        self.assertEqual(character.get_character_info()['inventory'], ['sword'])

    def test_take_bread(self):
        character.character_info['inventory'] = []
        character.set_column(5)
        character.set_row(5)
        map.set_map(5, 5, ' B ')
        take_item_check('take bread')
        self.assertEqual(character.get_character_info()['inventory'], ['bread'])

    def test_take_treasure(self):
        character.character_info['inventory'] = []
        character.set_column(5)
        character.set_row(5)
        map.set_map(5, 5, ' C ')
        take_item_check('take treasure')
        self.assertEqual(character.get_character_info()['inventory'], ['treasure'])

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_item_not_on_player(self, mock_output):
        character.character_info['inventory'] = []
        character.set_column(5)
        character.set_row(5)
        map.set_map(5, 5, ' C ')
        take_item_check('take bread')
        expected_output = 'You cant take that\n'
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    def test_item_not_on_player_returns_true(self):
        character.character_info['inventory'] = []
        character.set_column(5)
        character.set_row(5)
        map.set_map(5, 5, ' C ')
        self.assertTrue(take_item_check('take bread'))
