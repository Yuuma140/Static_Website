import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimeter, split_nodes_image, split_nodes_link

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

    def test_single_image(self):
        nodes = [
            TextNode("This is a text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        ]
        new_nodes = split_nodes_image(nodes)
        expected = [
            TextNode("This is a text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_single_link(self):
        nodes = [
            TextNode("This is a text with a [to boot dev](https://www.boot.dev)", TextType.TEXT)
        ]
        new_nodes = split_nodes_link(nodes)
        expected = [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_multiple_link(self):
        nodes = [
            TextNode("This is a text with a [to youtube](https://www.youtube.com/@bootdotdev) and with a [to boot dev](https://www.boot.dev)", TextType.TEXT)
        ]
        new_nodes = split_nodes_link(nodes)
        expected = [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            TextNode(" and with a ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_multiple_image(self):
        nodes = [
            TextNode("This is a text with an ![image](https://i.imgur.com/zjjcJKZ.png) and with a ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
        ]
        new_nodes = split_nodes_image(nodes)
        expected = [
            TextNode("This is a text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and with a ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_image(self):
        nodes = [
            TextNode("This is a text with no images", TextType.TEXT)
        ]  
        new_nodes = split_nodes_image(nodes)
        expected = [
            TextNode("This is a text with no images", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_link(self):
        nodes = [
            TextNode("This is a text with no links", TextType.TEXT)
        ]
        new_nodes = split_nodes_link(nodes)
        expected = [
            TextNode("This is a text with no links", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_text_type_text(self):
        nodes = [
            TextNode("This is an italic text", TextType.ITALIC)
        ]
        new_nodes = split_nodes_image(nodes)
        expected = [
            TextNode("This is an italic text", TextType.ITALIC)
        ]
        self.assertEqual(new_nodes, expected)

    def test_starting_with_image(self):
        nodes = [
            TextNode("![image](https://i.imgur.com/zjjcJKZ.png) This is an image", TextType.TEXT)
        ]
        new_nodes = split_nodes_image(nodes)
        expected = [
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" This is an image", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_starting_with_link(self):
        nodes = [
            TextNode("[to boot dev](https://www.boot.dev) This is a link", TextType.TEXT)
        ]
        new_nodes = split_nodes_link(nodes)
        expected = [
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" This is a link", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)