from enum import Enum

class TextType(Enum):
    normal= "normal"
    bold= "bold"
    italic= "italic"
    code= "code"
    link= "link"
    image= "image"

class TextNode():
    def __init__(self, text, text_type, url= None):
        self.text= text 
        self.text_type= TextType(text_type)
        self.url= url
    
    def __eq__(self, other_text_node):
        return (self.text== other_text_node.text and self.text_type.value== other_text_node.text_type.value and self.url== other_text_node.url)
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
