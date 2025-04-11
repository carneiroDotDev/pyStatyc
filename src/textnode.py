from enum import Enum
import typing as t

class TextType(Enum):
    BOLD = "bold"
    ITALICS = "italics"
    CODE = "code"
    IMAGE = "image"
    LINK = "link"

class TextNode:
    def __init__(self, text: str, textType: TextType, url: t.Optional[str] = None) -> None:
        self.text = text
        self.textType = textType
        self.url = url
        if not isinstance(text, str):
            raise ValueError("text must be a string")
        if not isinstance(textType, TextType):
            raise ValueError("textType must be an instance of TextType Enum")
        if url is not None and not isinstance(url, str):
            raise ValueError("url must be a string if provided")
        if textType == TextType.IMAGE and url is None:
            raise ValueError("url must be provided for IMAGE text type")
        if textType == TextType.LINK and url is None:
            raise ValueError("url must be provided for LINK text type")
    
    def __eq__(self, node: object) -> bool:
        if not isinstance(node, TextNode):
            return False
        return self.text == node.text and self.textType == node.textType and self.url == node.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.textType}, {self.url})"
