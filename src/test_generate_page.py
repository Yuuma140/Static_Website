import unittest
from generatepage import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        block = "# The title of the page"
        title = extract_title(block)
        self.assertEqual(title, "The title of the page")

    def test_extract_title_not_found(self):
        block = "This is not a title"
        with self.assertRaises(Exception):
            title = extract_title(block)

    def test_extract_title_two_heading(self):
        block = "## This is not a title"
        with self.assertRaises(Exception):
            title = extract_title(block)