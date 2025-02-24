from enum import Enum
from htmlnode import *
import re
from textnode import *

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case text_node.text_type.NORMAL:
            return LeafNode(None, text_node.text)
        case text_node.text_type.BOLD:
            return LeafNode("b",text_node.text)
        case text_node.text_type.ITALIC:
            return LeafNode("i",text_node.text)
        case text_node.text_type.CODE:
            return LeafNode("code",text_node.text)
        case text_node.text_type.LINKS:
            return LeafNode("a",text_node.text, {"href":text_node.url})
        case text_node.text_type.IMAGES:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        elif delimiter not in node.text:
            new_nodes.append(node)
        else:
            texts = node.text.split(delimiter)
            length = len(texts)
            if length > 1 and length % 2 == 0:
                raise Exception("Invalid markdown syntax")
            nodes = []
            for i in range(len(texts)):
                if texts[i] == "":
                    continue
                if i % 2 == 0:
                    nodes.append(TextNode(texts[i], TextType.NORMAL))
                else:
                    nodes.append(TextNode(texts[i], text_type))
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
        count = 0 
        images_list = extract_markdown_images(node_text)
        image_num = len(images_list)
        if image_num == 0:
            new_nodes.append(node)
            continue
        for image in images_list:
            alt_text, url = image
            sections = node_text.split(f"![{alt_text}]({url})", 1)
            if image_num == 1:
                nodes.append(TextNode(alt_text, TextType.IMAGES, url))
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if count == image_num:
                    nodes.append(TextNode(sections[i], TextType.NORMAL))
                if i == 0:
                    nodes.append(TextNode(sections[i], TextType.NORMAL))
                    nodes.append(TextNode(alt_text, TextType.IMAGES, url))
                    count += 1
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
                if i == 0 and sections[i] == "":
                    nodes.append(TextNode(text, TextType.LINKS, url))
                    continue
                if count == link_num:
                    nodes.append(TextNode(sections[i], TextType.NORMAL))
                if i % 2 == 0:
                    nodes.append(TextNode(sections[i], TextType.NORMAL))
                    nodes.append(TextNode(text, TextType.LINKS, url))
                    count += 1
                if i == 1:
                    node_text = sections[i] 
                    
        new_nodes.extend(nodes)
    return new_nodes


def text_to_text_nodes(text):
    node = [TextNode(text, TextType.NORMAL)]
    nodes = split_nodes_delimiter(node, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes , "`", TextType.CODE)
    nodes = split_nodes_link(split_nodes_image(nodes))
    return nodes


