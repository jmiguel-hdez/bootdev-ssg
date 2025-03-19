from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for i in range(len(blocks)):
        stripped = blocks[i].strip()
        if stripped != "":
            cleaned_blocks.append(stripped)
    return cleaned_blocks

def is_block_a_heading(block):
    pattern = r"^#{1,6}\s\S"
    match = re.match(pattern, block)
    if match:
        return True
    return False

def is_block_a_codeblock(block):
    lines = block.splitlines()
    if lines[0].startswith("```") and lines[-1].startswith("```"):
        return True
    return False

def is_block_a_quote(block):
    lines = block.splitlines()
    for l in lines:
        if not l.startswith('>'):
            return False
    return True

def is_block_an_unordered_list(block):
    lines = block.splitlines()
    for l in lines:
        if not l.startswith('- '):
            return False
    return True

def is_block_an_ordered_list(block):
    lines = block.splitlines()
    for i,l in enumerate(lines):
        if not l.startswith(f"{1+i}. "):
            return False
    return True

def block_to_block_type(block):
    if (is_block_a_heading(block)):
        return BlockType.HEADING

    if (is_block_a_codeblock(block)):
        return BlockType.CODE

    if (is_block_a_quote(block)):
        return BlockType.QUOTE

    if (is_block_an_unordered_list(block)):
        return BlockType.ULIST
    
    if (is_block_an_ordered_list(block)):
        return BlockType.OLIST

    return BlockType.PARAGRAPH