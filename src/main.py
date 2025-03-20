from copy_static import copy_src_to_dst
import os, shutil

static_path = "./static"
public_path = "./public"

def main():

    if os.path.exists(public_path):
        print("Deleting public directory...")
        shutil.rmtree(public_path)

    print("copy static files to public directory")
    copy_src_to_dst(static_path, public_path)

if __name__ == "__main__":
    main()