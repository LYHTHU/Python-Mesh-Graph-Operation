"""
    Converting .obj file to .stl, .ply, .off format for the processing.
    Author: Yunhao Li
"""

import os


def obj2off(path):
    out_path = save_path(path, ".off")


def obj2stl(path):
    out_path = save_path(path, ".stl")
    

def obj2ply(path):
    out_path = save_path(path, ".ply")


def traverse_convert(origin_path, target_path, func):
    if not os.path.exists(origin_path):
        print("Path {} does not exists!".format(origin_path))
        return
    



def save_path(origin, suffix):
    breakpoint = origin.rfind('/')
    dir_path = origin[:breakpoint]
    name = origin[breakpoint:origin.rfind('.')] +suffix
    save_path = os.path.join(dir_path+name)
    return save_path

if __name__ == "__main__":
    pass