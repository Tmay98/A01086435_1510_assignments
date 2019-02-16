from unittest import TestCase
from unittest.mock import patch
import dungeonsanddragons
import io


class TestAttack_player(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.generate_name', side_effect=['player1', 'player2'])
    @patch('dungeonsanddragons.roll_die', side_effect=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 3])
    @patch('builtins.input', side_effect=['barbarian', 'barbarian'])
    def test_attack_successful(self, mock_generate_name, mock_roll_die, mock_input, mock_stdout):
        attacker = dungeonsanddragons.create_character(5)
        defender = dungeonsanddragons.create_character(5)
        dungeonsanddragons.attack_player(attacker, defender)
        expected_output = 'player1 hit player2 for 3 damage\n player2 has 2 HitPoints left\n'
        output = mock_stdout.getvalue()
        self.assertEqual(expected_output, output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.generate_name', side_effect=['player1', 'player2'])
    @patch('dungeonsanddragons.roll_die', side_effect=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 3])
    @patch('builtins.input', side_effect=['barbarian', 'barbarian'])
    def test_attack_missed(self, mock_generate_name, mock_roll_die, mock_input, mock_stdout):
        attacker = dungeonsanddragons.create_character(5)
        defender = dungeonsanddragons.create_character(5)
        dungeonsanddragons.attack_player(attacker, defender)
        expected_output = 'player1 did not hit player2\n'
        output = mock_stdout.getvalue()
        self.assertEqual(expected_output, output)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('dungeonsanddragons.generate_name', side_effect=['player1', 'player2'])
    @patch('dungeonsanddragons.roll_die', side_effect=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 6])
    @patch('builtins.input', side_effect=['barbarian', 'barbarian'])
    def test_killed_defender(self, mock_generate_name, mock_roll_die, mock_input, mock_stdout):
        attacker = dungeonsanddragons.create_character(5)
        defender = dungeonsanddragons.create_character(5)
        dungeonsanddragons.attack_player(attacker, defender)
        expected_output = 'player1 hit player2 for 6 damage\n player2 died\n'
        output = mock_stdout.getvalue()
        self.assertEqual(expected_output, output)
