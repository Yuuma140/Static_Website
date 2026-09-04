import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "This is a link", None, {"href": "https://www.google.com", "target": "_blank"})
        actual = node.props_to_html()
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(actual, expected)

    def test_props_to_html_one(self):
        node = HTMLNode("h1", "This is a header", ["p", "b"], {"id": "header"})
        actual = node.props_to_html()
        expected = ' id="header"'
        self.assertEqual(actual, expected)

    def test_props_to_html_None(self):
        node = HTMLNode("h1", "This is a header", ["p", "b"])
        actual = node.props_to_html()
        expected = ""
        self.assertEqual(actual, expected)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click Me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hi!")
        self.assertEqual(node.to_html(), "Hi!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode(None, "plain text")
        child_node2 = LeafNode("b", "bold text")
        child_node3 = LeafNode("i", "italic text")
        parent_node = ParentNode("p", [child_node1, child_node2, child_node3])
        self.assertEqual(parent_node.to_html(), "<p>plain text<b>bold text</b><i>italic text</i></p>")

    def test_to_html_with_props(self):
        child_node = LeafNode("h1", "this is a header")
        parent_node = ParentNode("div", [child_node], {"class": "container", "id": "main"})
        self.assertEqual(parent_node.to_html(), '<div class="container" id="main"><h1>this is a header</h1></div>')

    def test_to_html_no_tag(self):
        child_node = LeafNode("b", "bold")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_mixed_siblings(self):
        child_node = LeafNode("p", "Hello world")
        parent_node = ParentNode("span", [child_node])
        grandparent_node = ParentNode("div", [child_node, parent_node])
        self.assertEqual(grandparent_node.to_html(), "<div><p>Hello world</p><span><p>Hello world</p></span></div>")