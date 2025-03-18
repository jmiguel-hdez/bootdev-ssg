from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType):
    new_nodes = []

    for node in old_nodes:
        match (node.text_type):
            case TextType.TEXT:
                dc = node.text.count(delimiter)
                if  dc % 2 != 0 or dc < 2:
                    raise Exception("invalid markdown syntax")
                splitted = node.text.split(delimiter)
                tmp_nodes = []
                for i,s in enumerate(splitted):
                    if i % 2 == 0:
                        tmp_nodes.append(TextNode(s, TextType.TEXT))
                    else:
                        tmp_nodes.append(TextNode(s, text_type))
                new_nodes.extend(tmp_nodes)
            case _:
                new_nodes.append(node)
    return new_nodes
