import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode("a",props={"href": "https://www.google.com", "target": "_blank"})
        print("--------------------")
        print("Props to HTML test")
        print(node.props_to_html())

    def test_print_node(self):
        node = HTMLNode("a",props={"href": "https://www.google.com", "target": "_blank"})
        print("--------------------")
        print("Node test")
        print(node)

    def test_leaf_to_html(self):
        leaf1 = LeafNode("p", "This is a paragraph of text.")
        leaf2 = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        print("--------------------")
        print("Leaf to html test")
        print(leaf1.to_html())
        print(leaf2.to_html())
        props = {"class": "my-class", "id": "unique-id"}
        leaf = LeafNode("div", "Content here", props)
        print(leaf.to_html())

    def test_parent_to_html(self):
        parent = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        LeafNode("a", "Click me!", props={"href": "https://www.google.com"}),
    ],
)
        print("--------------------")
        print("Parent to html test")
        print(parent.to_html())

    def test_parents_to_html(self):
        parent = ParentNode(
    "p",
    [
        ParentNode("t", [LeafNode("th", "Try this"), LeafNode("th", "Bold text")]),
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        LeafNode("a", "Click me!", props={"href": "https://www.google.com"}),
    ],
)
        print("--------------------")
        print("Parents to html test")
        print(parent.to_html())
    


if __name__ == "__main__":
    unittest.main()