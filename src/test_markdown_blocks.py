import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType

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

    def test_paragraph(self):
        block = "This is just a normal paragraph of text."
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_heading(self):
        block = "###### This is 6th heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_code(self):
        block = """```
        This is a code block
        ```"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)

    def test_quote(self):
        block = "> This is a quote"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_ul(self):
        block = "- This is an unordered list"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_ol(self):
        block = "1. This is an ordered list"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_seven_heading(self):
        block = "####### This is 7th heading but it's not heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_not_same_type(self):
        block = """> This is a quote
- This is not a quote"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_skipped_ordered_list(self):
        block = """1. This is first element of the ordered list
3. This is 3rd element not 2nd"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_missing_backticks(self):
        block = """```
        This a code block
        ``"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_one_heading(self):
        block = "# This is 1st Heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_start_at_second_ordered_list(self):
        block = """2. This starts at 2nd
3. This is another element"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_start_at_first_ordered_list(self):
        block = """1. This starts at 2nd
2. This is another element"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)