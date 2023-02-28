import sys
import time
import numpy as np
import cv2

import matplotlib.pyplot as plt



def main():
 
    
    original_points = np.loadtxt("org1.txt", delimiter=",")
    predicted_points = np.loadtxt("pred1.txt", delimiter=",")
    x =[p[0] for p in original_points]
    y =[p[1] for p in original_points]
    
    w =[m[0] for m in predicted_points[1:]]
    z =[m[1] for m in predicted_points[1:]]
    
    org_cols = original_points[1:,:2]
    pred_cols = predicted_points[1:,:2]

    error = np.sqrt(np.sum((pred_cols - org_cols)**2, axis=1))
    
    # # Calculate upper and lower bounds
    # upper_bound = org_cols + error[:, np.newaxis]
    # lower_bound = org_cols - error[:, np.newaxis]
    
    upper_bounds = org_cols + error.reshape(-1,1)
    lower_bounds = org_cols - error.reshape(-1,1)

    # Plot the data
    plt.plot(x, y, 'g-', label='Original Data')
    # plt.plot(w,z,'r-', label= 'Predicted Points')
    plt.fill_between(w, lower_bounds[:,1], upper_bounds[:,1], color='gray', alpha=0.2)
    plt.xlabel('X values')
    plt.ylabel('Y label')
    plt.legend()
    plt.show()
    
    
    # plt.plot(pred_cols[:, 0], pred_cols[:, 1], 'b', label='Predicted Data')
    # plt.fill_between(pred_cols[:, 0], upper_bound[:, 1], lower_bound[:, 1], color='gray', alpha=0.5, label='Error Bound')
    # plt.legend()
    # plt.show()
    # mean_error = np.mean(error)
    # print(mean_error)
    
    # plt.plot(x,y,'ro', label = 'original path')
    # plt.plot(w,z,'bo', label = 'predicted path')
    # plt.legend()
    # plt.show()
    
    

if __name__ == "__main__":
    main()