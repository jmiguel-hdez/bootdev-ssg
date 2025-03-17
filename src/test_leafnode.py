from leafnode import LeafNode
import unittest

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_p2(self):
        html = LeafNode("p", "This is a paragraph of text.").to_html()
        self.assertEqual(
            html,
            "<p>This is a paragraph of text.</p>"
        )
    
    def test_leaf_to_html_a(self):
        html = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(
            html,
            '<a href="https://www.google.com">Click me!</a>'
        )
    
    def test_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

if __name__ == '__main__':
    unittest.main()