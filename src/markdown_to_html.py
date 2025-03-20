from typing import List,Tuple
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType
)
from inline_markdown import text_to_textnodes
from pprint import pprint

def text_to_children(text: str) -> List[HTMLNode]:
    nodes = text_to_textnodes(text)
    html_nodes = []
    for node in nodes:
        html_nodes.append(text_node_to_html_node(node))
    
    return html_nodes
    
def text_heading_to_html_node(text):
    heading_level, remaining_text = text.split(" ", 1)
    children = text_to_children(remaining_text)
    heading_map = {
        "######":"h6",
        "#####":"h5",
        "####":"h4",
        "###":"h3",
        "##":"h2",
        "#":"h1",
        }
    tag = heading_map.get(heading_level, None)
    if not tag:
        raise ValueError("there was a problem parsing heading")
    return ParentNode(tag,children)

def text_paragraph_to_html_node(text):
    remaining_text = " ".join(text.split("\n"))
    children = text_to_children(remaining_text)
    tag = "p"
    return ParentNode(tag,children)

def text_quote_to_html_node(text):
    lines = []
    for l in text.split("\n"):
        lines.append(l.split(">", 1)[1])
    remaining_text = "\n".join(lines)
    children = text_to_children(remaining_text)
    tag = "blockquote"
    return ParentNode(tag,children)

def text_ulist_to_html_node(text):
    list_items = []
    for l in text.split("\n"):
        remaining_text = l.split("- ", 1)[1]
        children = text_to_children(remaining_text)
        tag = "li"
        list_items.append(ParentNode(tag,children))
    tag = "ul"
    return ParentNode(tag,list_items)

def text_olist_to_html_node(text):
    list_items = []
    for i,l in enumerate(text.split("\n")):
        remaining_text = l.split(f"{i}. ", 1)[1]
        children = text_to_children(remaining_text)
        tag = "li"
        list_items.append(ParentNode(tag,children))
    tag = "ol"
    return ParentNode(tag,list_items)

def text_code_to_html_node(text):
    lines = [l for l in text.split("\n") if not l.startswith("```")]
    lines.append("")
    remaining_text = "\n".join(lines)
    children = text_node_to_html_node(TextNode(remaining_text,TextType.CODE))

    return ParentNode("pre",[children])

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                 html_blocks.append(text_heading_to_html_node(block))
            case BlockType.CODE:
                 html_blocks.append(text_code_to_html_node(block))
            case BlockType.PARAGRAPH:
                 html_blocks.append(text_paragraph_to_html_node(block))
            case BlockType.QUOTE:
                 html_blocks.append(text_quote_to_html_node(block))
            case BlockType.OLIST:
                 html_blocks.append(text_olist_to_html_node(block))
            case BlockType.ULIST:
                 html_blocks.append(text_ulist_to_html_node(block))
    
    return ParentNode("div",html_blocks)