import unittest
from textnode import TextNode, TextType, text_node_to_html_node



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.bootdev.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.bootdev.dev")
        self.assertNotEqual(node, node2)
    
    def test_url_none_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.bootdev.dev")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic_bold_code(self):
        node_italic = TextNode("This is a italic node", TextType.ITALIC)
        node_bold = TextNode("This is a bold node", TextType.BOLD)
        node_code = TextNode("This is a code node", TextType.CODE)
        html_node_italic = text_node_to_html_node(node_italic)
        html_node_bold = text_node_to_html_node(node_bold)
        html_node_code = text_node_to_html_node(node_code)
        self.assertEqual(html_node_italic.tag, "i")
        self.assertEqual(html_node_italic.value, "This is a italic node")
        self.assertEqual(html_node_bold.tag, "b")
        self.assertEqual(html_node_bold.value, "This is a bold node")
        self.assertEqual(html_node_code.tag, "code")
        self.assertEqual(html_node_code.value, "This is a code node")


if __name__ == "__main__":
    unittest.main()