from enum import Enum
from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unorder_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")
    count = 0
    i = 1
    is_quote = True
    is_ul = True
    is_ol = True
    for char in block:
        if char == "#":
            count += 1
        else:
            break
    if count > 0 and count < 7 and block[count] == " ":
        return BlockType.HEADING
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE
    for line in lines:
        if not line.startswith("- "):
            is_ul = False
            break
    if is_ul:
        return BlockType.UNORDERED_LIST
    for line in lines:
        if not line.startswith(f"{i}. "):
            is_ol = False
            break
        else:
            i += 1
    if is_ol:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_blocks(text: str) -> list[str]:
    blocks = []
    splitted_text = text.split("\n\n")
    for txt in splitted_text:
        txt = txt.strip()
        if txt != "":
            blocks.append(txt)
    return blocks

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            heading_node = heading_to_html_node(block)
            block_nodes.append(heading_node)
        elif block_type == BlockType.PARAGRAPH:
            paragraph_node = paragraph_to_html_node(block)
            block_nodes.append(paragraph_node)
        elif block_type == BlockType.QUOTE:
            quote_node = quote_to_html_node(block)
            block_nodes.append(quote_node)
        elif block_type == BlockType.UNORDERED_LIST:
            ul_node = unordered_list_to_html_node(block)
            block_nodes.append(ul_node)
        elif block_type == BlockType.ORDERED_LIST:
            ol_node = ordered_list_to_html_node(block)
            block_nodes.append(ol_node)
        elif block_type == BlockType.CODE:
            pre_node = code_to_html_node(block)
            block_nodes.append(pre_node)
    parent_node = ParentNode("div", block_nodes)
    return parent_node

def text_to_children(text):
    new_nodes = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        node = text_node_to_html_node(node)
        new_nodes.append(node)
    return new_nodes

def heading_to_html_node(block):
    count = 0
    for char in block:
        if char == "#":
            count += 1
        else:
            break
    cleaned_text = block[count+1:]
    heading_node = ParentNode(f"h{count}", text_to_children(cleaned_text))
    return heading_node

def paragraph_to_html_node(block):
    cleaned_text = block.replace("\n", " ")
    paragraph_node = ParentNode("p", text_to_children(cleaned_text))
    return paragraph_node

def quote_to_html_node(block):
    lines = block.split("\n")
    cleaned_lines = []
    for line in lines:
        if line.startswith(">"):
            if line[1:].startswith(" "):
                cleaned_lines.append(line[2:])
            else:
                cleaned_lines.append(line[1:])
    cleaned_text = " ".join(cleaned_lines)
    quote_node = ParentNode("blockquote", text_to_children(cleaned_text))
    return quote_node

def unordered_list_to_html_node(block):
    lines = block.split("\n")
    list_items = []
    for line in lines:
        if line.startswith("- "):
            item_text = line[2:]
            li_node = ParentNode("li", text_to_children(item_text))
            list_items.append(li_node)
    ul_node = ParentNode("ul", list_items)
    return ul_node

def ordered_list_to_html_node(block):
    lines = block.split("\n")
    list_items = []
    i = 1
    for line in lines:
        if line.startswith(f"{i}. "):
            i += 1
            parts = line.split(". ", 1)
            item_text = parts[1]
            ol_li_node = ParentNode("li", text_to_children(item_text))
            list_items.append(ol_li_node)
    ol_node = ParentNode("ol", list_items)
    return ol_node

def code_to_html_node(block):
    cleaned_text = block[4:-3]
    plain_text = TextNode(cleaned_text, TextType.TEXT)
    code_leaf_node = text_node_to_html_node(plain_text)
    code_node = ParentNode("code", [code_leaf_node])
    pre_node = ParentNode("pre", [code_node])
    return pre_node
            