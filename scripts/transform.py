#!/usr/bin/env python
#!/usr/bin/env python3

#source: https://github.com/moble/quaternion 


import sys
import time
import numpy as np
import quaternion 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def transform_points(q_new,q_old,p_old):
    q_old_inv = np.conjugate(q_old)
    q_rot = q_new * q_old_inv     
    p_new = quaternion.rotate_vectors(q_rot,p_old)
    
    print("old quart:", q_old)
    print("new quart: ", q_new)
    print("old point: ", p_old)
    print("new point: ",p_new)
    
    """ Plot the points:
    
    """
    
    # fig = plt.figure(figsize=(12, 12))
    # ax = fig.add_subplot(projection='3d')
    
    # x_vals = [p_old[0],p_new[0]] 
    # y_vals = [p_old[1],p_new[1]] 
    # z_vals = [p_old[2],p_new[2]] 
    # ax.scatter(x_vals, y_vals, z_vals, c = 'b', marker='o')
    # ax.set_xlabel('X-axis')
    # ax.set_ylabel('Y-axis')
    # ax.set_zlabel('Z-axis')
    # plt.show()
    
    
def main():
    print("Transforming quarternions...")
    q_old = np.quaternion(1, 2, 3, 4)
    q_old_inv = np.conjugate(q_old) 
    q_new = np.quaternion(2.0, 2.0, 3.0, 4.0)
    p_old = [1.0,0.0,2.0]
    transform_points(q_new,q_old,p_old)
    
    

if __name__ == "__main__":
    main()
    
