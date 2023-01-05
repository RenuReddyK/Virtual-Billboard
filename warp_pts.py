import numpy as np
from est_homography import est_homography


def warp_pts(X, X_prime, interior_pts):
    """
    First compute homography from video_pts to logo_pts using X and X_prime,
    and then use this homography to warp all points inside the soccer goal

    Input:
        X: 4x2 matrix of (x,y) coordinates of goal corners in video frame
        X_prime: 4x2 matrix of (x,y) coordinates of logo corners in penn logo
        interior_pts: Nx2 matrix of points inside goal
    Returns:
        warped_pts: Nx2 matrix containing new coordinates for interior_pts.
        These coordinate describe where a point inside the goal will be warped
        to inside the penn logo. For this assignment, you can keep these new
        coordinates as float numbers.

    """

    # You should Complete est_homography first!
    H = est_homography(X, X_prime)

    ##### STUDENT CODE START #####
    N = interior_pts.shape[0]
    NEW_warped_pts = np.zeros((N,3))

    warped_pts = np.zeros((N,2))
    #new_interior_pts = [interior_pts[:,0],interior_pts[:,1],ones]
    # print(np.shape(new_interior_pts))
    for i in range(N):
        NEW_warped_pts[i] = np.matmul(H, np.array([interior_pts[i,0],interior_pts[i,1],1]))
    for i in range(N):
        warped_pts[i,0] = NEW_warped_pts[i,0]/NEW_warped_pts[i,2]
        warped_pts[i,1] = NEW_warped_pts[i,1]/NEW_warped_pts[i,2]
    
    ##### STUDENT CODE END #####

    return warped_pts
