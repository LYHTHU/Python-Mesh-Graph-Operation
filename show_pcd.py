import numpy as np
import open3d
import sys


def show_pcd(path):
    print("Showing \"{}\" .".format(path))
    raw = np.load(path)
    arr = raw[:, 0:3]
    color = []
    pcd = open3d.geometry.PointCloud()
    for i in range(raw[:, 3].size):
        if raw[i, 3] > 0:
            color.append([1, 0, 0])
        else:
            color.append([0, 0, 1])
    pcd.points = open3d.utility.Vector3dVector(arr)
    pcd.colors = open3d.utility.Vector3dVector(color)
    open3d.visualization.draw_geometries([pcd])


if  __name__ == "__main__":
    # path = sys.argv[1]
    path = "/home/yunhaoli/Desktop/Research/ShapeNet/TrainingData/03636649/4e0aabe8a65ddc43e019184dd4eea7e1/model_normalized.npy"
    show_pcd(path)