from unittest import TestCase
from sud import collision_check
from unittest.mock import patch
import io
import character
import map


class TestCollision_check(TestCase):

    def test_collision(self):
        map.reset_map()
        character.set_row(6)
        character.set_column(4)
        self.assertTrue(collision_check('north'))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_collision_message(self, mock_output):
        character.set_row(6)
        character.set_column(4)
        expected_output = 'You cant move in that direction\n'
        collision_check('north')
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    def test_move_north(self):
        character.set_row(7)
        character.set_column(4)
        self.assertFalse(collision_check('north'))

    def test_move_east(self):
        character.set_row(6)
        character.set_column(4)
        self.assertFalse(collision_check('east'))

    def test_move_south(self):
        character.set_row(6)
        character.set_column(4)
        self.assertFalse(collision_check('south'))

    def test_move_west(self):
        character.set_row(6)
        character.set_column(5)
        self.assertFalse(collision_check('west'))
