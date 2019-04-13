from unittest import TestCase
from backup import backup
import os
import io
from unittest.mock import patch


class TestBackup(TestCase):
    def test_backup(self):
        with open('random_file.txt', 'w') as f_obj:
            f_obj.write('random text')
        backup('random_file.txt')
        with open('random_file.bak', 'r') as f_obj:
            actual = f_obj.read()
        expected = 'random text'
        self.assertEqual(expected, actual)
        os.remove('random_file.txt')
        os.remove('random_file.bak')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_file_not_found(self, mock_output):
        backup('not_found.txt')
        expected = 'File not found\n'
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_backup_print_statement(self, mock_output):
        with open('random_file.txt', 'w') as f_obj:
            f_obj.write('random text')
        backup('random_file.txt')
        expected = 'generated random_file.bak\n'
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        os.remove('random_file.txt')
        os.remove('random_file.bak')
