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
