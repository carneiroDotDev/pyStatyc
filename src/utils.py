from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    """
    Splits a list of nodes into two lists based on a delimiter.

    :param old_nodes: The list of nodes to split.
    :param delimiter: The delimiter to split the nodes by.
    :param text_type: The type of text to split by (e.g., "text", "html").
    :return: A tuple containing two lists: the first list contains nodes before the delimiter,
             and the second list contains nodes after the delimiter.
    """
    for node in old_nodes:
        if delimiter not in node.text:
            raise Exception(f"Delimiter '{delimiter}' not found in node value '{node.text}'")
        #if node.textType != TextType.TEXT:
        #    raise Exception(f"Node text type '{node.textType}' for '{node}' is not TEXT")
    
    new_nodes = buildNewNodes(old_nodes, delimiter)
    return new_nodes
    
def buildNewNodes(old_nodes: list[TextNode], delimiter: str) -> list[TextNode]:
    """
    Helper function to build new nodes based on the delimiter.
    """
    new_nodes = []
    flag = False
    match(delimiter):
        case "`":
            for node in old_nodes:
                nodeTexts = node.text.split(delimiter)
                for text in nodeTexts:
                    if flag:
                        new_nodes.append(TextNode(text, TextType.CODE))
                    else:
                        new_nodes.append(TextNode(text, TextType.TEXT))
                    flag = not flag
            return new_nodes
        case "*" | "**":
            for node in old_nodes:
                nodeTexts = node.text.split(delimiter)
                for text in nodeTexts:
                    if flag:
                        new_nodes.append(TextNode(text, TextType.BOLD))
                    else:
                        new_nodes.append(TextNode(text, TextType.TEXT))
                    flag = not flag
            return new_nodes
        case "_":
            for node in old_nodes:
                nodeTexts = node.text.split(delimiter)
                for text in nodeTexts:
                    if flag:
                        new_nodes.append(TextNode(text, TextType.ITALIC))
                    else:
                        new_nodes.append(TextNode(text, TextType.TEXT))
                    flag = not flag
            return new_nodes
        case _:
            raise Exception(f"Delimiter '{delimiter}' not supported")
    

# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

# print(new_nodes)