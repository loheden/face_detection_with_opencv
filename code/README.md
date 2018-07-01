In this repository, 2 examples programs are provided to extract face images from given larger input images or webcam video streaming.

The program in the file face_detector_from_img.py reads images from the given path in the program and creates new face images in a separate directory. If a certain image includes multiples faces, the output from that image will then include all face images from the input image.

The file face_detector_from_webcam.py just takes the video streaming data from the computer webcam, extracts face images and saves these face images in a separate folder.

Both programs are only designed to detect images from the frontal position of the face (based on single cascade file) but additional haarcascade*.xml files can still be added to the programs to increase the chance of detecting the face from given inputs.

Both files can further be modified for the purpose of using in larger scale projects.
