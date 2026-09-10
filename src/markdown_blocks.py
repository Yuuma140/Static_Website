from enum import Enum

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