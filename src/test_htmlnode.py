
import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestLeafNode(unittest.TestCase):
    
    def test_leaf_to_html_p(self):
       node = LeafNode("p", "Hello, world!")
       self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
            
    def test_leaf_children_none(self):
        node = LeafNode("p", "Hello, world!", {})
        self.assertEqual(node.children, None)
        
        
class TestParentNode(unittest.TestCase):
    
    def test_parent_to_html(self):
        child1 = LeafNode("p", "Hello, world!")
        child2 = LeafNode("span", "This is a span.")
        parent = ParentNode("div", [child1, child2], {"class": "container"})
        expected_html = '<div class="container"><p>Hello, world!</p><span>This is a span.</span></div>'
        self.assertEqual(parent.to_html(), expected_html)
        
    def test_parent_children(self):
        child1 = LeafNode("p", "Hello, world!")
        child2 = LeafNode("span", "This is a span.")
        parent = ParentNode("div", [child1, child2], {"class": "container"})
        self.assertEqual(parent.children, [child1, child2])
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )