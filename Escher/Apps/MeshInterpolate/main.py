import sys
sys.path.append("../../")
from Geometry import Mesh
import ArapInterpolate 
from typing import List
import argparse
import os

def interpolate_from_paths(src_mesh_path:str, tgt_mesh_path:str, interval:float) -> List[Mesh]:
    src_mesh = Mesh(src_mesh_path)
    tgt_mesh = Mesh(tgt_mesh_path)

    src_mesh.load(process=False)
    tgt_mesh.load(process=False)

    _interpolated_meshes = ArapInterpolate.interpolate(src_mesh,tgt_mesh,interval)
    return _interpolated_meshes

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("src_mesh_path",help="Source mesh path to start interpolation",type=str)
    parser.add_argument("tgt_mesh_path",help="Target mesh path to end interpolation",type=str)
    parser.add_argument("destination_folder",help="Directory to store the interpolated meshes",type=str)
    parser.add_argument("--interval",help="Float value between 0 and 1, specifying interpolation spacing",type=float,default=0.1)

    args = parser.parse_args()
    interpolated_meshes = interpolate_from_paths(args.src_mesh_path,args.tgt_mesh_path,args.interval)

    if not os.path.exists(args.destination_folder):
        os.makedirs(args.destination_folder)

    for i,m in enumerate(interpolated_meshes):
        m.export(os.path.join(args.destination_folder,str(i)+'.obj'))