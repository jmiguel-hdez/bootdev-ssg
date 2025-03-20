from copy_static import copy_src_to_dst
from markdown_to_html import generate_pages_recursive

import os, shutil

static_path = "./static"
content_path = "./content"
public_path = "./public"
template_path = "./template.html"

def main():

    if os.path.exists(public_path):
        print("Deleting public directory...")
        shutil.rmtree(public_path)

    print("copy static files to public directory")
    copy_src_to_dst(static_path, public_path)
    generate_pages_recursive(content_path, template_path, public_path)

if __name__ == "__main__":
    main()