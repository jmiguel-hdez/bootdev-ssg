import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "a paragraph text", None, {"class": "primary"})
        self.assertEqual(
            repr(node),
            "HTMLNode('p','a paragraph text',None,{'class': 'primary'})"
        )

    def test_props(self):
        node = HTMLNode("a", "google.com", None, {"href":"https://www.google.com", "target":"_blank"})
        props = node.props_to_html()
        expect = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(props, expect)

    def test_props2(self):
        node = HTMLNode("a", "google.com")
        props = node.props_to_html()
        expect = ''
        self.assertEqual(props, expect)
    
    def test_values(self):
        node = HTMLNode("p", "a paragraph text")
        self.assertEqual(
            node.tag,
            "p"
        )

        self.assertEqual(
            node.value,
            "a paragraph text"
        )

        self.assertEqual(
            node.children,
            None,
        )

        self.assertEqual(
            node.props,
            None,
        )

    def test_to_html(self):
        node = HTMLNode("a", "google.com", None, {"href":"https://www.google.com", "target":"_blank"})
        self.assertRaises(NotImplementedError, node.to_html)

    def test_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

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
    
    def test_leaf_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_repr(self):
        node = LeafNode("a", "google.com", {"href":"https://www.google.com", "target":"_blank"})
        self.assertEqual(repr(node), "LeafNode('a','google.com',{'href': 'https://www.google.com', 'target': '_blank'})")
    
    def test_to_html_with_children2(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        html = node.to_html()
        self.assertEqual(
            html,
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

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
    
    def test_parent_node_repr(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            repr(parent_node),
            "ParentNode('div',[LeafNode('span','child',None)],None)"
        )
    
    def test_parent_node_no_children(self):
        parent_node = ParentNode("div", None, None)
        self.assertRaises(
            ValueError,
            parent_node.to_html,
        )

    def test_parent_node_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node], None)
        self.assertRaises(
            ValueError,
            parent_node.to_html,
        )

if __name__ == "__main__":
    unittest.main()