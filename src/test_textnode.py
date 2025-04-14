import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_unequal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode(
            "This is a different text node", TextType.ITALIC
        )
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        expected_repr = (
            "TextNode(This is a text node, TextType.BOLD, None)"
        )
        self.assertEqual(repr(node), expected_repr)

    def test_default_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)

    def test_with_url(self):
        node = TextNode(
            "This is a text node", TextType.LINK, "http://example.com"
        )
        self.assertEqual(node.url, "http://example.com")
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.textType, TextType.LINK)

    def test_invalid_text_type(self):
        with self.assertRaises(ValueError):
            TextNode("This is a text node", "invalid_text_type")

    def test_invalid_text_type_enum(self):
        with self.assertRaises(ValueError):
            TextNode(
                "This is a text node", TextType("invalid_text_type")
            )

    def test_invalid_url(self):
        with self.assertRaises(ValueError):
            TextNode("This is a text node", TextType.LINK, 12345)


if __name__ == "__main__":
    unittest.main()
