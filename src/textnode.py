from enum import Enum
from htmlnode import *
import re

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
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
        elif delimiter not in node.text:
            new_nodes.append(node)
        else:
            texts = node.text.split(delimiter)
            length = len(texts)
            if length > 1 and length % 2 == 0:
                raise Exception("Invalid markdown syntax")
            nodes = []
            count = 0
            for text in texts:
                if text == "":
                    continue
                if count % 2 == 0:
                    nodes.append(TextNode(text, TextType.NORMAL))
                    count += 1
                elif count % 2 != 0:
                    nodes.append(TextNode(text, text_type))
                    count += 1
            new_nodes.extend(nodes)
    return new_nodes

def extract_markdown_images(text):
    url_alt_text_tuples = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return url_alt_text_tuples

def extract_markdown_links(text):
    link_tuples = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_tuples
    
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        nodes = []
        node_text = node.text
        images_list = extract_markdown_images(node_text)
        if len(images_list) == 0:
            new_nodes.append(node)
            continue
        for image in images_list:
            alt_text, url = image
            sections = node_text.split(f"![{alt_text}]({url})", 1)
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    nodes.append(TextNode(sections[i], TextType.NORMAL))
                    nodes.append(TextNode(alt_text, TextType.IMAGES, url))
                if i == 1:
                    node_text = sections[i]

                    
        new_nodes.extend(nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        nodes = []
        node_text = node.text
        links_list = extract_markdown_links(node_text)
        link_num = len(links_list) 
        count = 0
        if len(links_list) == 0:
            new_nodes.append(node)
            continue
        for link in links_list:
            text, url = link
            sections = node_text.split(f"[{text}]({url})", 1)
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    nodes.append(TextNode(sections[i], TextType.NORMAL))
                    nodes.append(TextNode(text, TextType.LINKS, url))
                    count += 1
                if count == link_num:
                    nodes.append(TextNode(sections[i], TextType.NORMAL))
                if i == 1:
                    node_text = sections[i]

                    
        new_nodes.extend(nodes)
    return new_nodes






