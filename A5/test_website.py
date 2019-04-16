from unittest import TestCase
from website import website
from unittest.mock import patch
import os
import re


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

    @patch('builtins.input', side_effect=['tommy', 'info'])
    def test_website_contents(self, mock_input):
        website()
        with open('index.html') as f_obj:
            contents = f_obj.read()
        name_regex = re.compile(r'tommy')
        info_regex = re.compile(r'info')
        match_object_1 = name_regex.search(contents)
        match_object_2 = info_regex.search(contents)
        if not match_object_1 and match_object_2:
            self.fail()
        os.remove('index.html')


