import numpy as np


cos = np.cos; sin = np.sin
xd = np.array([1, 1, 0.5]) # Desired value in the Cartesian space
q = np.array([3, 3, 3]) # Initial value in the joint space
l = np.array([1, 1, 1])
epsilon = 1e-3
max_iter = 100 # Maximum number of iterations

# Iterations: Newton's method
for i in range(max_iter):
  q1 = q[0] ; q2 = q[1] ; q3 = q[2];
  l1 = l[0] ; l2 = l[1] ; l3 = l[2];
  f = np.array([cos(q1)*(l2*cos(q2) + (l3*cos(q2)*cos(q3))), 
                sin(q1)*(l2*cos(q2) + l3*cos(q2)*cos(q3)), 
                l1 + l2*sin(q2) + l3*sin(q2)*sin(q3)]) #Forward Kinematics
  J = np.array([[-sin(q1)*(l2*cos(q2)+l3*cos(q2)*cos(q3)), cos(q1)*(-l2*sin(q2)-l3*cos(q3)*sin(q2)), -l3*cos(q1)*cos(q2)*sin(q3)],
               [(l2*cos(q2)+l3*cos(q2)*cos(q3))*cos(q1), sin(q1)*(-l2*sin(q2)-l3*cos(q3)*sin(q2)), -l3*sin(q1)*cos(q2)*sin(q3)],
               [0, l2*cos(q2)+l3*cos(q2)*sin(q3), l3*sin(q2)*cos(q3)]])
  e = xd-f #Current Error
  q = q + np.dot(np.linalg.inv(J), e) #Dot product from 2 matrix

  # End condition
  if (np.linalg.norm(e) < epsilon): #If the diference is less than epsilon
    break

print(q)