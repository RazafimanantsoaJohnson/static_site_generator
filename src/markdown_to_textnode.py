from textnode import TextNode, TextType
from splitting_functions import split_nodes_delimiter, split_nodes_image, split_nodes_link
import re

def markdown_to_blocks(markdown):
    # BE more focused in the details they give us (definition)
    blocks= list(
                filter(lambda line: line!="", markdown.split("\n\n"))
            )
    block_markdown=[]
    for block in blocks:
        block_markdown.append(block.strip())
    print("==================testiii=========")
    print(block_markdown)
    print("=======================")
    return block_markdown   


def text_to_textnode(md_text):
    # Turn the md_text into a textnode, pass it to the delimiter, take the result and pass it to the delimiter with other
    # texttypes, we will go through all of them 
    # TEXT, BOLD, ITALIC, IMAGE, LINK, CODE, NORMAL
    splitted_with_bold= split_nodes_delimiter([TextNode(md_text, TextType.TEXT)],'**', TextType.BOLD)
    splitted_with_italic= split_nodes_delimiter(splitted_with_bold, '*', TextType.ITALIC)
    splitted_with_code= split_nodes_delimiter(splitted_with_italic, '`', TextType.CODE)
    splitted_with_images= split_nodes_image(splitted_with_code)
    final_result= split_nodes_link(splitted_with_images)
    return final_result
