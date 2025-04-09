from enum import Enum
import typing as t

class TextType(Enum):
    BOLD = "bold"
    ITALICS = "italics"
    CODE = "code"
    IMAGE = "image"
    LINK = "link"

class TextNode:
    def __init__(self, text: str, textType, url: str | None = None) -> None:
        self.text = text
        self.textType = textType
        self.url = url
    
    def __eq__(self, node: object) -> bool:
        if not isinstance(node, TextNode):
            return False
        return self == node

    def __repr__(self):
        return f"TextNode({self.text}, {self.textType}, {self.url})"
