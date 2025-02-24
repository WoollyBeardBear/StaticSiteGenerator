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
    htmlnode = markdown_to_htmlnode(markdown)
    html = htmlnode.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    
    with open(dest_path, "w") as dest:
        dest.write(template)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # list content contents
    content = os.listdir(dir_path_content)

    # crawl the content. If its an md file then generate page, if its a dir then recurse into the directory
    for object in content:
        content_path = dir_path_content + f"/{object}"
        dest_path = dest_dir_path + f"/{object}"
        if os.path.isdir(content_path):
            os.mkdir(dest_path)
            generate_pages_recursive(content_path, template_path, dest_path)
        if content_path.endswith(".md"):
            dest_path = dest_path[:-3] + ".html"
            generate_page(content_path, template_path, dest_path)

