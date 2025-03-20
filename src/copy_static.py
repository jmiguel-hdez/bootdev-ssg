import os
import shutil

def copy_src_to_dst(src, dst):
    
    if not os.path.exists(src):
        raise ValueError(f"{src} doesn't exist, invalid parameter")

    print(f"copy_src_to_dst({src}, {dst})")

    #create directory
    if not os.path.exists(dst):
        print(f"mkdir {dst}")
        os.mkdir(dst)

    for f in os.listdir(src):
        from_path = os.path.join(src,f)
        dest_path = os.path.join(dst, f)
        if os.path.isfile(from_path):
            print(f" * copy {from_path} to {dest_path}")
            shutil.copy(from_path, dest_path)
        else:
            copy_src_to_dst(from_path, dest_path)

