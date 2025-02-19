import unittest
from block_markdown import *

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = (
            "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        )
        print("--------------------------")
        print("Markdown to Blocks")
        print(markdown_to_blocks(markdown))

    def test_block_type(self):
        block1 = "### This is a heading!"
        print("-------------------------")
        print("Block Type Test")
        print (f"{block1}")
        print(block_to_block_type(block1))
        block2 = "``` This is a code block ```"
        print (f"{block2}")
        print(block_to_block_type(block2))
        block3 = "> quote item\n> another quote item\n> a thrid list item"
        print (f"{block3}")
        print(block_to_block_type(block3))
        block4 = "1. item one\n2. item two\n3. item three"
        print (f"{block4}")
        print(block_to_block_type(block4))
        block5 = "* item one\n item two\n* item three"
        print (f"{block5}")
        print(block_to_block_type(block5))

    def test_to_htmlnode(self):
        markdown = ("### This is a **bold heading** it should have a few children [to google](www.google.com) lets see!\n\n"
                    + "```def main:\n\tprint('hello world')```\n\n"
                    + "> Man does not live on bread alone\n> but on every word that comes from the mouth of God\n\n"
                    + "* He said goodbye\n* I said hello\n* hello hello\n\n"
                    + "This is just a noraml old paragraph BORING not even a single bold word")
        print("-------------------------")
        print("markdown to htmlnodes")
        print(markdown_to_htmlnode(markdown)) 