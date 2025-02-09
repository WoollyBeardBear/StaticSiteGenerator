import unittest

from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_type_eq(self):
        node = TextNode("This is a different", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.text_type, node2.text_type)

    def test_diff_text(self):
        node = TextNode("This is a different", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node.text, node2.text)
    
    def test_node_to_node(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Hello There", TextType.LINKS, "https://www.google.com")
        node3 = TextNode("This is a picture of a cat licking itself", TextType.IMAGES, "https://images.app.goo.gl/E5UVZKKDpEzy2hwA8")
        print("________________________")
        print("TextNode to HTMLNode test!")
        htmlnode1 = text_node_to_html_node(node1)
        print(f"{node1} to {htmlnode1}")
        htmlnode2 = text_node_to_html_node(node2)
        print(f"{node2} to {htmlnode2}")
        htmlnode3 = text_node_to_html_node(node3)
        print(f"{node3} to {htmlnode3}")

    def test_split_delimiter(self):
        print("--------------------------")
        print("Split Node Delimiter Test")
        nodes = [
            TextNode("This is text with a `code block` word and a second `code block number two`", TextType.NORMAL),
            TextNode("This is a text with a **bolded phrase**", TextType.NORMAL),
            TextNode("THIS WHOLE THING IS BOLDED AND **SHOULDNT** BE SPLIT UP", TextType.BOLD)
        ]
        code_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        bold_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        print(f"code nodes {code_nodes}")
        print(f"bold nodes {bold_nodes}")


if __name__ == "__main__":
    unittest.main()