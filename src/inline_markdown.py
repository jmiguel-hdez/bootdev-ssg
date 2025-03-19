from textnode import TextType, TextNode
from typing import List, Tuple
import re

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType):
    new_nodes = []
    for node in old_nodes:
        match (node.text_type):
            case TextType.TEXT:
                sections = node.text.split(delimiter)
                if len(sections) % 2 == 0:
                    raise ValueError("invalid markdown syntax, section not closed")
                split_nodes = []
                for i,s in enumerate(sections):
                    if s == "":
                        continue
                    if i % 2 == 0:
                        split_nodes.append(TextNode(s, TextType.TEXT))
                    else:
                        split_nodes.append(TextNode(s, text_type))
                new_nodes.extend(split_nodes)
            case _:
                new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text: str) -> List[Tuple[str, str]]:
    # images
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text: str) -> List[Tuple[str, str]]:

    # regular links
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    pattern = r"(!\[[^\[\]]*\]\([^\(\)]*\))"
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = re.split(pattern, old_node.text)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown syntax")
        for i,s in enumerate(sections):
            if s == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(s, TextType.TEXT))
            else:
                images = extract_markdown_images(s)
                split_nodes.append(TextNode(images[0][0], TextType.IMAGE, images[0][1]))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    pattern = r"(?<!!)(\[[^\[\]]*\]\([^\(\)]*\))"
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = re.split(pattern, old_node.text)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown syntax")
        for i,s in enumerate(sections):
            if s == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(s, TextType.TEXT))
            else:
                links = extract_markdown_links(s)
                split_nodes.append(TextNode(links[0][0], TextType.LINK, links[0][1]))
        new_nodes.extend(split_nodes)
    return new_nodes