import shutil
from textnode import TextNode, TextType
import os
from copy_static import *
from generate_page import *

from_path, dest_path = "./content/index.md", "./public/index.html"

def main():
    copy_static()
    generate_page(from_path, "template.html", dest_path)
    

main()
