from copy_static import copy_src_to_dst
from markdown_to_html import generate_page

import os, shutil

static_path = "./static"
public_path = "./public"
index_path = "./content/index.md"
template_path = "./template.html"
output = os.path.join(public_path,"index.html")

def main():

    if os.path.exists(public_path):
        print("Deleting public directory...")
        shutil.rmtree(public_path)

    print("copy static files to public directory")
    copy_src_to_dst(static_path, public_path)
    generate_page(index_path, template_path, output)

if __name__ == "__main__":
    main()