import unittest
from textnode import TextType, TextNode

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

if __name__=="__main__":
    unittest.main()
