from textnode import TextType, TextNode

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
