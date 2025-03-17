import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "a paragraph text")
        representation = str(node)
        self.assertTrue(representation.find("HTMLNode(") != -1)

    def test_props(self):
        node = HTMLNode("a", "google.com", None, {"href":"https://www.google.com", "target":"_blank"})
        props = node.props_to_html()
        expect = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(props, expect)

    def test_to_html(self):
        node = HTMLNode("a", "google.com", None, {"href":"https://www.google.com", "target":"_blank"})
        self.assertRaises(NotImplementedError, node.to_html)

    def test_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)