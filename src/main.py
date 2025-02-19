import shutil
from textnode import TextNode, TextType
import os

def main():
    TN = TextNode("HELLO THERE", TextType.BOLD, "https://www.boot.dev")
    print(TN)
    copy_tree("./static")



def copy_tree(path, times=0):
    times += 1
    dst_base_dir = "./public"
    new_path = ""
    if os.path.exists("./public") and times == 0:
        shutil.rmtree("./public")
        os.mkdir("./public")
        new_path = "./public"
    static_dir = os.listdir(path)
    for object in static_dir:
        current_path = path + f"/{object}"
        new_path += f"/{object}"
        print(f"current path: {current_path}, new path: {new_path}")
        if os.path.isdir(current_path):
            print(f"{current_path} is a directory")
            os.mkdir(os.path.join(dst_base_dir, new_path))
            copy_tree(current_path, times)
        else:
            print(f"current path: {current_path}, new path: {new_path}")
            shutil.copy(current_path, new_path)
            
            
    
    

main()
