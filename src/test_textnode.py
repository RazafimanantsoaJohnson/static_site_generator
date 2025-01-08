import unittest
from textnode import TextType, TextNode
from htmlnode import LeafNode
from textnode_to_htmlnode import text_node_to_html_node
from splitting_functions import split_nodes_delimiter
from markdown_to_textnode import text_to_textnode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node= TextNode("This is a text node", TextType.BOLD)
        node2= TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq2(self):
        # Different text_type and text_content
        node1= TextNode("My text node", TextType.CODE, "http://jojo.co")
        node2= TextNode("Another text node", TextType.IMAGE)
        self.assertNotEqual(node1,node2)
    def test_eq3(self):
        node1= TextNode("My text node", TextType.IMAGE, "./src/jojo.jpeg")
        node2= TextNode("My text node", TextType.IMAGE)
        self.assertNotEqual(node1,node2)

    def test_textnode_to_text_conversion(self):
        leafnode= LeafNode(None, "Some text")
        textnode= TextNode("Some text", TextType.TEXT)
        converted_text_node= text_node_to_html_node(textnode)
        self.assertEqual(str(converted_text_node), str(leafnode))
    def test_textnode_to_image_conversion(self):
        leafnode= LeafNode("img", "",{"alt":"Some image", "src": "http://coolimg.com"})
        textnode= TextNode("Some image", TextType.IMAGE,'http://coolimg.com' )
        converted_text_node= text_node_to_html_node(textnode)
        self.assertEqual(str(converted_text_node), str(leafnode))

    def test_split_nodes_with_non_text(self):
        nodes=[
            TextNode("A simple link node", TextType.LINK, "http:/my_page_special.com"),
            TextNode("A simple code node", TextType.CODE )
        ]
        expected_nodes= [
            TextNode("A simple link node", TextType.LINK, "http:/my_page_special.com"),
            TextNode("A simple code node", TextType.CODE )
        ]
        self.assertListEqual(split_nodes_delimiter(nodes, '*', TextType.ITALIC), expected_nodes)

    def test_split_nodes_with_single_text_arg(self):
        nodes= [
            TextNode("This part should turn into a text node *this should be italic* This should be text node again", TextType.TEXT, None)
        ]
        expected_nodes= [
            TextNode("This part should turn into a text node ", TextType.TEXT, None),
            TextNode('this should be italic', TextType.ITALIC, None),
            TextNode(" This should be text node again", TextType.TEXT, None) 
        ]
        self.assertListEqual(split_nodes_delimiter(nodes, '*', TextType.ITALIC), expected_nodes)

    def test_split_nodes_with_many_args(self):
        nodes= [
            TextNode("This part should turn into a text node *this should be italic* This should be text node again", TextType.TEXT, None),
            TextNode("A simple link node", TextType.LINK, "http:/my_page_special.com"),
            TextNode("A simple code node", TextType.CODE )
        ]
        expected_nodes= [
            TextNode("This part should turn into a text node ", TextType.TEXT, None),
            TextNode('this should be italic', TextType.ITALIC, None),
            TextNode(" This should be text node again", TextType.TEXT, None),
            TextNode("A simple link node", TextType.LINK, "http:/my_page_special.com"),
            TextNode("A simple code node", TextType.CODE )
        ]
        self.assertListEqual(split_nodes_delimiter(nodes,'*', TextType.ITALIC), expected_nodes)

    # Boot.dev tests
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_text_to_textnode(self):
        md_text= "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result= text_to_textnode(md_text)
        expected_result= [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(expected_result, result)

    def test_text_to_textnodes2(self):
        nodes = text_to_textnode(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )



if __name__=="__main__":
    unittest.main()
