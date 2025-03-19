from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType
)
import unittest
from pprint import pprint

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_markdown_to_blocks_2(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
            ],
        )


    def test_block_to_block_type(self):
        md = """
## This is a heading

```python
print("hello, world!")
```

> this is
> a quote
>block

- this is an item
- this is another item
- this is a third item

1. this is an item
2. this is another item
3. this is a third item




This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""
        blocks = markdown_to_blocks(md)
        types = [block_to_block_type(b) for b in blocks]
        self.assertEqual(
            types,
            [
                BlockType.HEADING,
                BlockType.CODE,
                BlockType.QUOTE,
                BlockType.ULIST,
                BlockType.OLIST,
                BlockType.PARAGRAPH,
                BlockType.ULIST,
            ],
        )

if __name__ == "__main__":
    unittest.main()