import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimeter

class TestSplitNodesDelimeter(unittest.TestCase):
    def test_single_delimeter_pair(self):
        node = TextNode("hello *world* goodbye", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "*", TextType.ITALIC)
        expected = [
            TextNode("hello ", TextType.TEXT),
            TextNode("world", TextType.ITALIC),
            TextNode(" goodbye", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_unclosed_delimeter_raises(self):
        node = TextNode("hello *world goodbye", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimeter([node], "*", TextType.ITALIC)

    def test_multiple_delimeter_pair(self):
        node = TextNode("This is an *italic word* and this is also an *italic word*, bye", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "*", TextType.ITALIC)
        expected = [
            TextNode("This is an ", TextType.TEXT),
            TextNode("italic word", TextType.ITALIC),
            TextNode(" and this is also an ", TextType.TEXT),
            TextNode("italic word", TextType.ITALIC),
            TextNode(", bye", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_bold_and_italic_chained(self):
        node = TextNode("This is **bold** and _italic_ text", TextType.TEXT)
        nodes = split_nodes_delimeter([node], "**", TextType.BOLD)
        nodes = split_nodes_delimeter(nodes, "_", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected)

    def test_non_text_node_unchanged(self):
        node = TextNode("already bold", TextType.BOLD)
        new_nodes = split_nodes_delimeter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [node])

    def test_no_delimeter_present(self):
        node = TextNode("just plain text here", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [node])

    def test_delimeter_at_start(self):
        node = TextNode("*italic* at the start", TextType.TEXT)
        new_nodes = split_nodes_delimeter([node], "*", TextType.ITALIC)
        expected = [
            TextNode("italic", TextType.ITALIC),
            TextNode(" at the start", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_multiple_input_nodes(self):
        nodes = [
            TextNode("already bold", TextType.BOLD),
            TextNode("some *italic* text", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimeter(nodes, "*", TextType.ITALIC)
        expected = [
            TextNode("already bold", TextType.BOLD),
            TextNode("some ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)