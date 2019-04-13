from unittest import TestCase
from website import website
from unittest.mock import patch
import os


class TestWebsite(TestCase):

    @patch('builtins.input', side_effect=['tommy', 'info'])
    def test_website_index_created(self, mock_input):
        website()
        try:
            with open('index.html') as f_obj:
                pass
        except FileNotFoundError:
                self.fail('file wasnt created')
        os.remove('index.html')

