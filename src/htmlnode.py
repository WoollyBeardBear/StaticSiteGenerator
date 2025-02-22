

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html = ""
        for key in self.props:
            html = html + f' {key}="{self.props[key]}"'
        return html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        props = props or {}
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Must include value")
        if self.tag == None:
            return f"{self.value}"
        if self.props == None:
            print("props == None")
            return f"<{self.tag}>{self.value}</{self.tag}> "
        
        html = f"<{self.tag}" + self.props_to_html() + f"> {self.value}</{self.tag}> "
        return html
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Must include tag")
        if not self.children:
            raise ValueError("Must include children")
        
        html = f"<{self.tag}>"
        if isinstance(self.children, list):
            for child in self.children:
                html = html + f"{child.to_html()}"
        else:
            html = html + f"{self.children}"
        html = html + f"</{self.tag}>"
        return html
