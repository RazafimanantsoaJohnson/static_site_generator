from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images
from extract_markdown_links import extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # Check the text_type if != TEXT just return the nodes as is, checking if there only one occurence of the delimiter
    # raise an error if that's the case, We have to take into account the length of my delimiter
    new_nodes= []
    for node in old_nodes:
        if node.text_type!= TextType.TEXT:
            new_nodes.append(node)
        else:
            # Our error was to assume there will only be one 'sub node' per text
            splitted_nodes= []
            delimited_node_texts= node.text.split(delimiter)
            if len(delimited_node_texts)%2 ==0:
                raise Exception("Invalid number of occurences of delimiter in the original text")
            for i in range(len(delimited_node_texts)):
                if delimited_node_texts[i]== "":
                    continue
                elif i %2 == 0:
                    splitted_nodes.append(TextNode(delimited_node_texts[i], node.text_type))
                else:
                    splitted_nodes.append(TextNode(delimited_node_texts[i], text_type))
            new_nodes.extend(splitted_nodes)

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


    # We have at least, 0 images, at most as many images as there are texts (if the text ends with an image), normally


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes
