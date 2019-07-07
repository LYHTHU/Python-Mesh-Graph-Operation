"""
    Converting .obj file to .stl, .ply, .off format for the processing.
    Using trimesh
    Author: Yunhao Li
"""


import os
import trimesh


def obj2off(path):
    out_path = save_path(path, ".off")
    obj = trimesh.load_mesh(path)
    obj.export(out_path, file_type="off")


def obj2stl(path):
    out_path = save_path(path, ".stl")
    obj = trimesh.load_mesh(path)
    obj.export(out_path, file_type="stl")


def obj2ply(path):
    out_path = save_path(path, ".ply")
    obj = trimesh.load_mesh(path)
    obj.export(out_path, file_type="ply")


def traverse_convert(origin_path, target_path, func):
    if not os.path.exists(origin_path):
        print("Path {} does not exists!".format(origin_path))
        return

    if not os.path.exists(target_path):
        os.makedirs(target_path)
    


def save_path(origin, suffix):
    breakpoint = origin.rfind('/')
    dir_path = origin[:breakpoint]
    name = origin[breakpoint:origin.rfind('.')] +suffix
    save_path = os.path.join(dir_path+name)
    return save_path

if __name__ == "__main__":
    obj_path = "./data/tube.obj"
    obj2ply(obj_path)