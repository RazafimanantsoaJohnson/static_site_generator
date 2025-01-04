# from textnode and will turn into html

class HTMLNode():

    def __init__(self, tag= None, value= None, children= None, props= None):
        self.tag= tag
        self.value= value
        self.children= children
        self.props= props

    def to_html(self):
        # a method that will be implemented in child classes
        raise NotImplementedError()
    
    def props_to_html(self):
        result= ""
        if self.props != None:
            for key in self.props.keys():
                result+= f" {key}=\"{self.props[key]}\""
            return result
        else:
            return ""
    
    def __repr__(self):
        # These methods are very useful for debugging
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {str(self.props)})"
    
class LeafNode(HTMLNode):

    def __init__(self,tag, value, props= None ):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("This leaf node has no value impossible")
        elif self.tag== None:
            return f"{self.value}"
        else:
            if self.tag != None:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            else:
                return f"{self.value}"

class ParentNode(HTMLNode):

    def __init__(self,tag, children, props=None):
        super().__init__(tag,None, children, props)

    def to_html(self):
        if self.children == None or self.children== []:
            raise ValueError("A parent node can't have missing children")
        elif self.value != None:
            raise ValueError("A parent node can't have value")
        else:
            children_html=""
            for child in self.children:
                children_html+= child.to_html()
            if self.tag != None:
                return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
            else:
                return f"{children_html}"