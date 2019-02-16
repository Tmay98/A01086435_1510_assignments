from unittest import TestCase
from unittest.mock import patch
import dungeonsanddragons


class TestCombat_round(TestCase):

    @patch('dungeonsanddragons.generate_name', side_effect=['player1', 'player2'])
    @patch('dungeonsanddragons.roll_die', side_effect=[7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 10, 2, 10, 3])
    @patch('builtins.input', side_effect=['barbarian', 'barbarian'])
    def test_hp_reduction(self, mock_generate_name, mock_roll_die, mock_input):
        expected_output = ''
        character_1 = dungeonsanddragons.create_character(5)
        character_2 = dungeonsanddragons.create_character(5)
        dungeonsanddragons.combat_round(character_1, character_2)
        character_1_hp = character_1['HitPoints'] == 4
        character_2_hp = character_2['HitPoints'] == 3
        self.assertTrue(character_1_hp and character_2_hp)

    def test_incorrect_character_input(self):
        with self.assertRaises(TypeError):
            dungeonsanddragons.combat_round(5, 3)

