
import typing as t

class HTMLNode:
    """
    A class representing a node in an HTML document.
    """

    def __init__(self, tag: t.Optional[str]  = None, value: t.Optional[str]  = None, props: t.Optional[dict] = None, children: t.Optional[list["HTMLNode"]] = None) -> None:
        """
        Initializes an HTMLNode with a tag, attributes, and children.

        :param tag: The HTML tag of the node.
        :param value: The text content of the node.
        :param children: A list of child nodes.
        :param props: A dictionary of attributes for the node.
        """
        self.tag = tag
        self.value = value
        self.props = props
        self.children = children

        
        if not isinstance(tag, (str, type(None))):
            raise ValueError("tag must be a string")
        if props is not None and not isinstance(props, dict):
            raise ValueError("props must be a dictionary")
        if not isinstance(value, (str, type(None))):
            raise ValueError("value must be a string or None")
        if not isinstance(children, (list, type(None))):
            raise ValueError("children must be a list or None")
        if children is not None and not all(isinstance(child, HTMLNode) for child in children):
            raise ValueError("all children must be HTMLNode instances")

    def to_html(self):
        """
        Converts the HTMLNode to an HTML string representation.

        :return: The HTML string representation of the node.
        """
        raise NotImplementedError("Subclasses should implement this method")
        # Example implementation:
        # if self.tag is None:
        #     return self.value or ""
        # opening_tag = f"<{self.tag}"
        # if self.props:
        #     props_str = " ".join([f'{key}="{value}"' for key, value in self.props.items()])
        #     opening_tag += f" {props_str}"
        # opening_tag += ">"
        # closing_tag = f"</{self.tag}>"
        # if self.children:
        #     children_str = "".join(child.to_html() for child in self.children)
        # else:
        #     children_str = self.value or ""
        # return f"{opening_tag}{children_str}{closing_tag}"

    def props_to_html(self):
        """
        Converts the props dictionary to an HTML string representation.

        :return: The HTML string representation of the props.
        """
        if self.props:
            return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
        return ""
    
    def __repr__(self):
        """
        Returns a string representation of the HTMLNode.

        :return: A string representation of the HTMLNode.
        """
        return f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props}, children={self.children})"
    
    def __eq__(self, value):
        """
        Compares two HTMLNode objects for equality.

        :param value: The other HTMLNode to compare with.
        :return: True if the nodes are equal, False otherwise.
        """
        if not isinstance(value, HTMLNode):
            return False
        return (self.tag == value.tag and
                self.value == value.value and
                self.props == value.props and
                self.children == value.children)