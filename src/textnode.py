from enum import Enum
from htmlnode import *

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node2):
        if (self.text == text_node2.text and 
            self.text_type == text_node2.text_type and 
            self.url == text_node2.url):
            return True
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case text_node.text_type.NORMAL:
            return LeafNode(None, text_node.text)
        case text_node.text_type.BOLD:
            return LeafNode("<b>",text_node.text)
        case text_node.text_type.ITALIC:
            return LeafNode("<i>",text_node.text)
        case text_node.text_type.CODE:
            return LeafNode("<code>",text_node.text)
        case text_node.text_type.LINKS:
            return LeafNode("<a>",text_node.text, {"href":text_node.url})
        case text_node.text_type.IMAGES:
            return LeafNode("<img>", "", {"src": text_node.url, "alt": text_node.text})