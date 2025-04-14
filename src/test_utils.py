import unittest
from utils import buildNewNodes, split_nodes_delimiter
from textnode import TextNode, TextType


class Test_test_split_nodes_delimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self) -> None:
        # Test case 1: Basic splitting
        old_nodes = [
            TextNode(
                "This is text with a `code block` word", TextType.TEXT
            )
        ]
        delimiter = "`"
        text_type = TextType.TEXT
        result = split_nodes_delimiter(old_nodes, delimiter, text_type)
        expected_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(result, expected_result)

        # Test case 2: Delimiter not found
        # old_nodes = [TextNode("Hello world!", TextType.TEXT)]
        # delimiter = ","
        # text_type = TextType.TEXT
        # with self.assertRaises(Exception):
        #     split_nodes_delimiter(old_nodes, delimiter, text_type)


class Test_test_buildNewNodes(unittest.TestCase):
    def test_buildNewNodes(self) -> None:
        # Test case 1: Basic splitting
        old_nodes = [
            TextNode(
                "This is text with a `code block` word", TextType.TEXT
            )
        ]
        delimiter = "`"
        result = buildNewNodes(old_nodes, delimiter)
        expected_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(result, expected_result)
        # Test case 2: Delimiter not found
        # old_nodes = [TextNode("Hello world!", TextType.TEXT)]
        # delimiter = ","
        # with self.assertRaises(Exception):
        #     buildNewNodes(old_nodes, delimiter)
        # Test case 3: Multiple delimiters
        old_nodes = [
            TextNode("This is text with a *bold* word", TextType.TEXT)
        ]
        delimiter = "*"
        result = buildNewNodes(old_nodes, delimiter)
        expected_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(result, expected_result)
        # Test case 4: Empty input
        old_nodes = []
        delimiter = "*"
        result = buildNewNodes(old_nodes, delimiter)
        expected_result = []
        self.assertEqual(result, expected_result)
        # Test case 5: No delimiters
        old_nodes = [TextNode("No delimiters here", TextType.TEXT)]
        delimiter = "*"
        result = buildNewNodes(old_nodes, delimiter)
        expected_result = [
            TextNode("No delimiters here", TextType.TEXT)
        ]
        self.assertEqual(result, expected_result)
