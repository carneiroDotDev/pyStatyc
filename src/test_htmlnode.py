
import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_eq(self):
        node = HTMLNode("div", "This is a div", {"class": "container"})
        node2 = HTMLNode("div", "This is a div", {"class": "container"})
        self.assertEqual(node, node2)

    def test_unequal(self):
        node = HTMLNode("div", "This is a div", {"class": "container"}, [])
        node2 = HTMLNode("span", "This is a different div", {"class": "container"}, [])
        self.assertNotEqual(node, node2)
        
    def test_repr(self):
        node = HTMLNode("div", "This is a div", {"class": "container"}, [])
        expected_repr = "HTMLNode(tag=div, value=This is a div, props={'class': 'container'}, children=[])"
        self.assertEqual(repr(node), expected_repr)
        
    def test_invalid_tag(self):
        with self.assertRaises(ValueError):
            HTMLNode(123, "This is a div", {"class": "container"}, [])
            
    def test_invalid_props(self):
        with self.assertRaises(ValueError):
            HTMLNode("div", "This is a div", "invalid_props", [])
            
    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            HTMLNode("div", 123, {"class": "container"}, [])
            
    def test_invalid_children(self):
        with self.assertRaises(ValueError):
            HTMLNode("div", "This is a div", {"class": "container"}, "invalid_children")
            
    def test_props_to_html(self):
        node = HTMLNode("div", "This is a div", {"class": "container"}, [])
        expected_props_str = 'class="container"'
        self.assertEqual(node.props_to_html(), expected_props_str)
    def test_props_to_html_empty(self):
        node = HTMLNode("div", "This is a div", {}, [])
        expected_props_str = ''
        self.assertEqual(node.props_to_html(), expected_props_str)
    def test_props_to_html_none(self):
        node = HTMLNode("div", "This is a div", None, [])
        expected_props_str = ''
        self.assertEqual(node.props_to_html(), expected_props_str)
