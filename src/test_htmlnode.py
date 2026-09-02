import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "This is a link", None, {"href": "https://www.google.com", "target": "_blank"})
        actual = node.props_to_html()
        expected = " href=https://www.google.com target=_blank"
        self.assertEqual(actual, expected)

    def test_props_to_html_one(self):
        node = HTMLNode("h1", "This is a header", ["p", "b"], {"id": "header"})
        actual = node.props_to_html()
        expected = " id=header"
        self.assertEqual(actual, expected)

    def test_props_to_html_None(self):
        node = HTMLNode("h1", "This is a header", ["p", "b"])
        actual = node.props_to_html()
        expected = ""
        self.assertEqual(actual, expected)