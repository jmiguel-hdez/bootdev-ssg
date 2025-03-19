def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for i in range(len(blocks)):
        stripped = blocks[i].strip()
        if stripped != "":
            cleaned_blocks.append(stripped)
    return cleaned_blocks