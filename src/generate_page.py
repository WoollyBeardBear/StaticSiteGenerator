from inline_markdown import *
from htmlnode import *
from textnode import *
from block_markdown import *
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as t:
        template = t.read()
    html = markdown_to_htmlnode(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    
    with open(dest_path, "w") as dest:
        dest.write(template)
    

