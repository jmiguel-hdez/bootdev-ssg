class HTMLNode():
    def __init__(self, tag: str=None, value: str=None, children:list =None, props: dict=None):
        """Initialize an HTMLNode instance.

        Args:
            tag (str, optional): A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
            value (str, optional): A string representing the value of the HTML tag (e.g. the text inside a paragraph)
            children (list[HTMLNode], optional): A list of HTMLNode objects representing the children of this node
            props (dict, optional): A dictionary of key-value pairs representing the attributes of the HTML tag. 
                                    For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props = [f' {k}="{v}"' for k,v in self.props.items()]
        return "".join(props)
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag!r},{self.value!r},{self.children!r},{self.props!r})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.children is not None:
            raise ValueError("LeafNode can't have children")
        if self.tag is None:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag!r},{self.value!r},{self.props!r})"