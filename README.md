# Virtual-Billboard


https://user-images.githubusercontent.com/68454938/210884177-89fed08e-8b9c-4ca0-a669-d65ab96d8ecf.mov


Used the concepts of projective geometry and homographies to project an image onto a scene (here projecting Upenn logo onto the football goal post).

By using the images from a video sequence of a football match, the corners of the Penn Engineering logo and the corners of the goal in each image, homography is computed between the logo and the goal. It may seem that the correct way to calculate the homography would be to map the points from the logo image onto the video frame. But this will lead to holes in the image as it might lead to a state where multiple logo points are mapped to one video frame pixel while other logo points may not have any logo points at all. To avoid this situation inverse homography is calculated to find the projection from video frame points to logo points which guarantees that every video frame pixel gets a corresponding pixel from the logo. Then the goal points are warped onto the ones in the logo to generate a projection of the logo onto the video frame.
