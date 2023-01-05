import numpy as np


def est_homography(X, X_prime):
    """
    Calculates the homography of two planes, from the plane defined by X
    to the plane defined by X_prime. In this assignment, X are the coordinates of the
    four corners of the soccer goal while X_prime are the four corners of the penn logo

    Input:
        X: 4x2 matrix of (x,y) coordinates of goal corners in video frame
        X_prime: 4x2 matrix of (x,y) coordinates of logo corners in penn logo
    Returns:
        H: 3x3 homogeneours transformation matrix s.t. X_prime ~ H*X

    """

    ##### STUDENT CODE START #####
    x = X[:, 0]
    y = X[:, 1]
    xP = X_prime[:, 0]
    yP = X_prime[:, 1]
    ax=np.zeros([4,9])
    ay=np.zeros([4,9])
    A = []
    for i in range(X.shape[0]):
        A.append([-x[i], -y[i], -1, 0, 0, 0, x[i]*xP[i], y[i]*xP[i], xP[i]])
        A.append([0, 0, 0, -x[i], -y[i], -1, x[i]*yP[i], y[i]*yP[i], yP[i]])
    A = np.array(A)
    [U, S, Vt] = np.linalg.svd(A)
    h = np.transpose(Vt)[:,-1]
    H = h.reshape(3,3)

    ##### STUDENT CODE END #####

    return H
