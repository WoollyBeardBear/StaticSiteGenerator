import shutil
from textnode import TextNode, TextType
import os

def main():
    copy_static()


    
            
def copy_static():
    # Clean destination once
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    os.mkdir("./public")
    # Start the recursive copy
    _copy_recursive("./static", "./public")
    print("copy static complete")

def _copy_recursive(src, dst):
    static_dir = os.listdir(src)
    for object in static_dir:
        current_path = src + f"/{object}"
        new_path = dst + f"/{object}"
        if os.path.isdir(current_path):
            os.mkdir(new_path)
            _copy_recursive(current_path, new_path)
        else:
            shutil.copy(current_path, new_path)
    

main()
