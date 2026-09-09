import unittest
from markdown_blocks import markdown_to_blocks

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]
        )

    def test_multiple_newlines_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph



This is another paragraph with 4 newlines break
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with 4 newlines break",
            ]
        )

    def test_leading_and_trailing_whitespaces(self):
        md = """
This is a **bolded** paragraph

    This is another paragraph with leading and trailing whitespaces 
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a **bolded** paragraph",
                "This is another paragraph with leading and trailing whitespaces",
            ]
        )

    def test_single_block(self):
        md = """
        This is single block of the markdown document
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is single block of the markdown document",
            ]
        )