from textnode import TextNode, TextType
from htmlnode import HTMLNode,LeafNode

def text_node_to_html_node(textnode: TextNode):
    match textnode.text_type:
        case TextType.TEXT: 
            return LeafNode(None, textnode.text)
        case TextType.BOLD:
            return LeafNode("b", textnode.text)
        case TextType.ITALIC: 
            return LeafNode("i", textnode.text)
        #code, link, image
        case TextType.CODE:
            return LeafNode("code", textnode.text)
        case TextType.LINK:
            return LeafNode("a", textnode.text, {"href": textnode.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"alt": textnode.text, "src": textnode.url})
        case _:
            raise Exception("This text node has no text type")
