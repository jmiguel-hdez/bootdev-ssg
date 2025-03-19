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
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        
        images = extract_markdown_images(old_node.text)
        if not images:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text
        for alt_text,url in images:
            image_markdown = f"![{alt_text}]({url})"
            parts = remaining_text.split(image_markdown, 1)

            if parts[0]:
                split_nodes.append(TextNode(parts[0], TextType.TEXT))

            split_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

            if len(parts) > 1:
                remaining_text = parts[1]

        if remaining_text:
            split_nodes.append(TextNode(remaining_text, TextType.TEXT))

        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        remaining_text = old_node.text
        links = extract_markdown_links(remaining_text)

        if not links:
            new_nodes.append(old_node)
            continue

        for link, url in links:
            markdown_link = f"[{link}]({url})"
            parts = remaining_text.split(markdown_link, 1)

            if parts[0]:
                split_nodes.append(TextNode(parts[0], TextType.TEXT))

            split_nodes.append(TextNode(link, TextType.LINK, url))

            if len(parts) > 1:
                remaining_text = parts[1]
        if remaining_text:
            split_nodes.append(TextNode(remaining_text, TextType.TEXT))

        new_nodes.extend(split_nodes)
    return new_nodes


def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(new_nodes,"`", TextType.CODE)
    new_nodes = split_nodes_delimiter(new_nodes,"_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes,"**", TextType.BOLD)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes