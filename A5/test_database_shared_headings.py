from unittest import TestCase
from database_shared_headings import database_shared_headings


class TestDatabase_shared_headings(TestCase):
    def test_database_shared_headings(self):
        database = {'person1': {'surname': 'sdfb', 'name': 'dfgd', 'notes': 'dsfsd'},
                    'person2': {'surname': 'dsfsd', 'name': 'sdfsd', 'notes': 'sdfs', 'author': 'sdfsd'}
                    }
        expected = database_shared_headings(database)
        actual = ['surname', 'name', 'notes']
        self.assertEqual(expected, actual)

    def test_no_similar_keys(self):
        database = {'person1': {'surname': 'sdfb', 'name': 'dfgd', 'notes': 'dsfsd'},
                    'person2': {'stuff': 'dsfsd', 'author': 'sdfsd'}
                    }
        expected = database_shared_headings(database)
        actual = []
        self.assertEqual(expected, actual)

    def test_all_shared_keys(self):
        database = {'person1': {'surname': 'sdfb', 'name': 'dfgd', 'notes': 'dsfsd'},
                    'person2': {'surname': 'dsfsd', 'name': 'sdfsd', 'notes': 'sdfs'}
                    }
        expected = database_shared_headings(database)
        actual = ['surname', 'name', 'notes']
        self.assertEqual(expected, actual)
