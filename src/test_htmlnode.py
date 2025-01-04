import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_create_htmlnode(self):
        htmlnode= HTMLNode("p", "My first html node value", [], {"href": "http://some_link.com", "alt": "some funny images"})
        expected_result= f"HTMLNode(p, My first html node value, [], {str({"href": "http://some_link.com", "alt": "some funny images"})})"
        self.assertEqual(expected_result,str(htmlnode))

    def test_props_to_html(self):
        htmlnode= HTMLNode("p", "My first html node value", [], {"href": "http://some_link.com", "alt": "some funny images"})
        expected_result= " href=\"http://some_link.com\" alt=\"some funny images\""
        self.assertEqual(htmlnode.props_to_html(), expected_result)
    
    def test_create_leafnode(self):
        leafnode= LeafNode("p","This is a leaf paragraph node ")
        expected_result= f"HTMLNode(p, This is a leaf paragraph node , None, None)"
        self.assertEqual(str(leafnode), expected_result )
    
    def test_create_leafnode2(self):
        leafnode= LeafNode("p","This is a leaf paragraph node ")
        expected_result= f"<p>This is a leaf paragraph node </p>"
        self.assertEqual(leafnode.to_html(), expected_result)
    
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_create_parent_node(self):
        node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
        expected_result= "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_result)

    def test_nested_parent_node(self):
        node = ParentNode(
                "p",
                [
                    ParentNode("p",[LeafNode("b", "Bold text")],{"color": "purple", "bg": "darkgrey"}),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    ParentNode("p",[
                        ParentNode("h2",[LeafNode(None,"some h2 text")]),
                        LeafNode("b", "Bold text")
                        ],{"color": "purple", "bg": "cyan"}),
                    LeafNode(None, "Normal text"),
                ],
            )
        expected_result= f"<p><p color=\"purple\" bg=\"darkgrey\"><b>Bold text</b></p>Normal text<i>italic text</i><p color=\"purple\" bg=\"cyan\"><h2>some h2 text</h2><b>Bold text</b></p>Normal text</p>"
        print(expected_result)
        self.assertEqual(node.to_html(),expected_result)
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__=="__main__":
    unittest.main()