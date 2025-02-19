from inline_markdown import *
from enum import Enum
from htmlnode import *
import re
from textnode import *

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered = list(filter(lambda x: x.strip() != "", blocks))
    return filtered

def block_to_block_type(block):
    # code
    if block[:3] == "```" and block[-3:] == "```":
        return "code"
    # heading
    heading_count = 0
    for i in range(0, 8):
        if block[i].startswith("#"):
            heading_count += 1
    if heading_count >= 1 and heading_count <= 6:
        return "heading"
    # quote
    split_blocks = block.split("\n")
    split_length = len(split_blocks)
    quote_count = 0
    for block in split_blocks:
        if block.startswith(">"):
            quote_count += 1
    if quote_count == split_length:
        return "quote"
    # unordered list
    uo_list_count = 0
    for block in split_blocks:
        if block.startswith("* ") or block.startswith("- "):
            uo_list_count += 1
    if uo_list_count == split_length:
        return "unordered_list"
    # ordered list
    expected_number = 1
    for block in split_blocks:
        if block.startswith(f"{expected_number}. "):
            expected_number += 1
        else:
            return "paragraph"
    return "ordered_list"
    
        
def markdown_to_htmlnode(markdown):
    blocks = markdown_to_blocks(markdown)
    final_htmlnodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case "heading":
                stripped_block = block.lstrip("# ")
                heading_count = len(block) - len(stripped_block)
                heading_htmlnodes = ParentNode(f"<h{heading_count}>", text_to_children(stripped_block))
                final_htmlnodes.append(heading_htmlnodes)
            case "code":
                block = block.strip("`")
                code_htmlnodes = ParentNode("<code>", text_to_children(block))
                pre_code_htmlnodes = ParentNode("<pre>", code_htmlnodes)
                final_htmlnodes.append(pre_code_htmlnodes)
            case "quote":
                cleaned_quote_block = block.replace(">", "").strip()
                quote_htmlnodes = ParentNode("<blockquote>",text_to_children(cleaned_quote_block))
                final_htmlnodes.append(quote_htmlnodes)
            case "unordered_list":
                uolist_split = block.strip().split("\n")
                list_nodes = []
                for line in uolist_split:
                    cleaned_line = line.lstrip("* ")
                    list_nodes.append(HTMLNode("<li>", text_to_children(cleaned_line)))
                uolist_htmlnodes = ParentNode("<ul>", list_nodes)
                final_htmlnodes.append(uolist_htmlnodes)
            case "ordered_list":
                lines = block.split("\n").strip()
                list_nodes = []
                line_num = 1
                for line in lines:
                    list_nodes.append(HTMLNode("<li>", text_to_children(line.lstrip(f"{line_num}. "))))
                    line_num += 1
                olist_htmlnodes = ParentNode("<ol>", list_nodes)
                final_htmlnodes.append(olist_htmlnodes)
            case "paragraph":
                paragraph_nodes = ParentNode("<p>", text_to_children(block))
                final_htmlnodes.append(paragraph_nodes)
    return ParentNode("<div>", final_htmlnodes)
                

def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    htmlnodes = []
    for textnode in text_nodes:
        htmlnode = text_node_to_html_node(textnode)
        htmlnodes.append(htmlnode)
    return htmlnodes

