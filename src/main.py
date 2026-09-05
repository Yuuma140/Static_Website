from textnode import TextType, TextNode

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.bootdev.dev")
    print(node)


if __name__ == "__main__":
    main()