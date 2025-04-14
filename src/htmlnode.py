import typing as t
from textnode import TextType, TextNode


class HTMLNode:
    """
    A class representing a node in an HTML document.
    """

    def __init__(
        self,
        tag: t.Optional[str] = None,
        value: t.Optional[str] = None,
        props: t.Optional[dict] = None,
        children: t.Optional[list["HTMLNode"]] = None,
    ) -> None:
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
        if children is not None and not all(
            isinstance(child, HTMLNode) for child in children
        ):
            raise ValueError("all children must be HTMLNode instances")

    def to_html(self) -> str:
        """
        Converts the HTMLNode to an HTML string representation.

        :return: The HTML string representation of the node.
        """
        raise NotImplementedError(
            "Subclasses should implement this method"
        )
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

    def props_to_html(self) -> str:
        """
        Converts the props dictionary to an HTML string representation.

        :return: The HTML string representation of the props.
        """
        if self.props:
            return " ".join(
                [
                    f'{key}="{value}"'
                    for key, value in self.props.items()
                ]
            )
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
        return (
            self.tag == value.tag
            and self.value == value.value
            and self.props == value.props
            and self.children == value.children
        )


class LeafNode(HTMLNode):
    """
    A class representing a leaf node in an HTML document.
    """

    def __init__(
        self,
        tag: t.Optional[str],
        value: str,
        props: t.Optional[dict] = None,
    ) -> None:
        """
        Initializes a LeafNode with a tag and attributes.

        :param tag: The HTML tag of the node.
        :param value: The text content of the node.
        :param props: A dictionary of attributes for the node.
        As a leaf node, it does not have children.
        """
        super().__init__(tag, value, props)

    def to_html(self) -> str:
        """
        Converts the LeafNode to an HTML string representation.
        :return: The HTML string representation of the node.
        """

        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        opening_tag = f"<{self.tag}"
        if self.props:
            props_str = " ".join(
                [
                    f'{key}="{value}"'
                    for key, value in self.props.items()
                ]
            )
            opening_tag += f" {props_str}"
        opening_tag += ">"
        closing_tag = f"</{self.tag}>"
        return f"{opening_tag}{self.value}{closing_tag}"


class ParentNode(HTMLNode):
    """
    A class representing a parent node in an HTML document.
    """

    def __init__(
        self,
        tag: str,
        children: list[HTMLNode] = [],
        props: t.Optional[dict[str, str | int]] = None,
    ) -> None:
        """
        Initializes a ParentNode with a tag, props, and children.

        :param tag: The HTML tag of the node.
        :param props: A dictionary of attributes for the node.
        :param children: A list of child nodes.
        """
        super().__init__(tag, None, props, children)

    def to_html(self) -> str:
        """
        Converts the ParentNode to an HTML string representation.

        :return: The HTML string representation of the node.
        """
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        opening_tag = f"<{self.tag}"

        if self.props:
            props_str = " ".join(
                [
                    f'{key}="{value}"'
                    for key, value in self.props.items()
                ]
            )
            opening_tag += f" {props_str}"
        opening_tag += ">"
        closing_tag = f"</{self.tag}>"
        children_str = "".join(
            child.to_html() for child in self.children
        )
        return f"{opening_tag}{children_str}{closing_tag}"


def text_node_to_html_node(node: TextNode) -> HTMLNode:
    """
    Converts a TextNode to an HTMLNode.

    :param node: The TextNode to convert.
    :return: The converted HTMLNode.
    """
    match (node.textType):
        case TextType.TEXT:
            return LeafNode(None, node.text)
        case TextType.BOLD:
            return LeafNode("b", node.text)
        case TextType.ITALIC:
            return LeafNode("i", node.text)
        case TextType.CODE:
            return LeafNode("code", node.text)
        case TextType.IMAGE:
            if node.url is None:
                raise ValueError(
                    "URL must be provided for IMAGE text type"
                )
            return LeafNode(
                "img", "", {"src": node.url, "alt": node.text}
            )
        case TextType.LINK:
            if node.url is None:
                raise ValueError(
                    "URL must be provided for LINK text type"
                )
            return LeafNode("a", node.text, {"href": node.url})
        case _:
            raise ValueError(f"Unsupported text type: {node.textType}")
