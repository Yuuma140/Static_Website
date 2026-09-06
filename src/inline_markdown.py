from textnode import TextNode, TextType
import re

def split_nodes_delimeter(old_nodes: list[TextNode], delimeter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            if delimeter in node.text:
                result = node.text.split(delimeter)
                if len(result) % 2 == 0:
                    raise Exception("Delimeter is unclosed in the node")
                else:
                    for i, chunk in enumerate(result):
                        if i % 2 == 0:
                            if chunk != "":
                                new_nodes.append(TextNode(chunk, TextType.TEXT))
                        else:
                            if chunk != "":
                                new_nodes.append(TextNode(chunk, text_type))
            else:
                new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text: str):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
    


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches