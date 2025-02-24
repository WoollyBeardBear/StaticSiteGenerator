import shutil
from textnode import TextNode, TextType
import os
from copy_static import *
from generate_page import *

d_path = "hello.md"

def main():
    copy_static()
    generate_pages_recursive("./content", "./template.html", "./public")
    

main()
