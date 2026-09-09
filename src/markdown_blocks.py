def markdown_to_blocks(text: str) -> list[str]:
    blocks = []
    splitted_text = text.split("\n\n")
    for txt in splitted_text:
        txt = txt.strip()
        if txt != "":
            blocks.append(txt)
    return blocks