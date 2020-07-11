import unittest
from unittest.mock import patch
from unittest import TestCase
import string_manipulation


class Test(TestCase):

    # get_input will return 'yes' during this test
    @patch('string_manipulation.get_input', return_value='Bubble')
    def test_string_manipulation_with_letters(self, input):
        self.assertEqual(string_manipulation.string_processing(), "ulebbb")

    @patch('string_manipulation.get_input', return_value='1234345611')
    def test_string_manipulation_with_numbers(self, input):
        self.assertEqual(string_manipulation.string_processing(), "2563344111")

    @patch('string_manipulation.get_input', return_value='akdjf244da')
    def test_string_manipulation_with_alphanumeric(self, input):
        self.assertEqual(string_manipulation.string_processing(), "kjf2aadd44")

    @patch('string_manipulation.get_input', return_value='!@#@@afdf2324s')
    def test_string_manipulation_with_special_characters(self, input):
        self.assertEqual(string_manipulation.string_processing(), "!#ad34sff22@@@")

    @patch('string_manipulation.get_input', return_value='')
    def test_string_manipulation_with_empty_string(self, input):
        self.assertEqual(string_manipulation.string_processing(), "")


if __name__ == '__main__':
    unittest.main()