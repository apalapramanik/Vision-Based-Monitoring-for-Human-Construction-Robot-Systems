import numpy as np
import matplotlib.pyplot as plt

# Load the original points and predicted points
original_points = np.loadtxt("org1.txt", delimiter=",")
predicted_points = np.loadtxt("pred1.txt", delimiter=",")

# Extract the x and y values for original points
x = [p[0] for p in original_points]
y = [p[1] for p in original_points]

# Extract the x and y values for predicted points
w = [m[0] for m in predicted_points[1:]]
z = [m[1] for m in predicted_points[1:]]

# Calculate the error between each predicted point and original point
error = np.sqrt(np.sum((predicted_points[1:, :2] - original_points[1:, :2])**2, axis=1))

# Calculate the upper bound by adding the error
upper_bound = original_points[1:, :2] + error[:, np.newaxis]

# Calculate the lower bound by subtracting the error
lower_bound = original_points[1:, :2] - error[:, np.newaxis]

# Plot the original points, predicted points, and bounds
plt.plot(x, y, 'r-', label='Original Points')
plt.plot(w, z, 'b-', label='Predicted Points')
plt.plot(upper_bound[:, 0], upper_bound[:, 1], 'gray', label='Upper Bound')
plt.plot(lower_bound[:, 0], lower_bound[:, 1], 'gray', label='Lower Bound')
plt.legend()
plt.show()

# original_points = np.loadtxt("org1.txt", delimiter=",")
# predicted_points = np.loadtxt("pred1.txt", delimiter=",")

# org_cols = original_points[:,:2]
# pred_cols = predicted_points[:,:2]

# error = np.sqrt(np.sum((pred_cols - org_cols)**2, axis=1))
# upper_bound = org_cols + error.reshape(-1,1)
# lower_bound = org_cols - error.reshape(-1,1)

# plt.plot(org_cols[:,0], org_cols[:,1], 'b', label='Original')
# plt.plot(pred_cols[:,0], pred_cols[:,1], 'r', label='Predicted')
# plt.fill_between(org_cols[:,0], upper_bound[:,1], lower_bound[:,1], color='gray', alpha=0.5)
# plt.legend(loc='upper left')
# plt.show()