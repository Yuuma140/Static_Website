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

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        original_text = node.text
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            matches = extract_markdown_images(original_text)
            if len(matches) == 0:
                new_nodes.append(node)
            else:
                remaining_text = original_text
                for alt, url in matches:
                    sections = remaining_text.split(f"![{alt}]({url})", 1)
                    if sections[0] != "":
                        new_nodes.append(TextNode(sections[0], TextType.TEXT))
                    new_nodes.append(TextNode(alt, TextType.IMAGE, url))
                    remaining_text = sections[1]
                if remaining_text != "":
                    new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes
                    

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        original_text = node.text
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            matches = extract_markdown_links(original_text)
            if len(matches) == 0:
                new_nodes.append(node)
            else:
                remaining_text = original_text
                for link, url in matches:
                    sections = remaining_text.split(f"[{link}]({url})", 1)
                    if sections[0] != "":
                        new_nodes.append(TextNode(sections[0], TextType.TEXT))
                    new_nodes.append(TextNode(link, TextType.LINK, url))
                    remaining_text = sections[1]
                if remaining_text != "":
                    new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimeter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimeter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimeter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes