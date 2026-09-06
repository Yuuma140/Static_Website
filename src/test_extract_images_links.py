from inline_markdown import extract_markdown_images, extract_markdown_links
import unittest

class TestExtractImagesLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://www.boot.dev)"
        )
        self.assertListEqual([("link", "https://www.boot.dev")], matches)

    def test_extract_multiple_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)

    def test_extract_multiple_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_no_images(self):
        matches = extract_markdown_images(
            "This is plain text without any images or links."
        )
        self.assertListEqual([], matches)
    
    def test_extract_links_ignores_images(self):
        matches = extract_markdown_links(
            "Here is an ![image](https://example.com/img.png) and a [link](https://example.com)."
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_extract_images_ignores_links(self):
        matches = extract_markdown_images(
            "Here is an ![image](https://example.com/img.png) and a [link](https://example.com)."
        )
        self.assertListEqual([("image", "https://example.com/img.png")], matches)

    def test_consecutive_links(self):
        matches = extract_markdown_links(
            "[first](https://first.com)[second](https://second.com)"
        )
        self.assertListEqual([("first", "https://first.com"), ("second", "https://second.com")], matches)

    def test_empty_alt_text(self):
        matches = extract_markdown_images(
            "An image with no alt text: ![](https://example.com/img.png)"
        )
        self.assertListEqual([("", "https://example.com/img.png")], matches)

    def test_broken_syntax(self):
        matches = extract_markdown_links(
            "This [link is broken](https://missing-closing-bracket.com"
        )
        self.assertListEqual([], matches)