from markdown_blocks import markdown_to_html_node
from htmlnode import HTMLNode
import os
from pathlib import Path

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line[1:].strip()
            return title
    raise Exception("no title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        from_path_content = file.read()
        from_path_html = markdown_to_html_node(from_path_content).to_html()
    with open(template_path, 'r') as file:
        template_path_content = file.read()
    title = extract_title(from_path_content)
    page = template_path_content
    page = page.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", from_path_html)
    destination_directory = os.path.dirname(dest_path)
    os.makedirs(destination_directory, exist_ok = True)
    with open(dest_path, 'w') as file:
        page = file.write(page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for content in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, content)
        dest_path = os.path.join(dest_dir_path, content)
        if not os.path.isfile(from_path):
            generate_pages_recursive(from_path, template_path, dest_path)
        else:
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)