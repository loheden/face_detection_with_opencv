"""
This program reads the video stream from the Webcam of the computer,
detects faces (using opencv) in the streaming data and saves detected face 
image files in a directory as configured below.
"""

# import opencv
import cv2


out_directory = '/home/cesncn/Desktop/github_projects/face_detect_with_opencv/code/face_imgs_from_webcam/'

#the program uses a face detector that uses a classfier based on frontal positon of face
def detectFace(faceDetector, vid):
    while(True):
        ret, img = vid.read()
        counter=1
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            sub_face = img[y:y+h, x:x+w]
            face_file_name = "face_" + str(y) + ".jpg"
            counter=counter+1
            cv2.imwrite((out_directory+face_file_name), sub_face)
        cv2.imshow('frame',img)
        cv2.imwrite( "Gray_Image.jpg", img);
        
        #print(x,y,w,h)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

vid = cv2.VideoCapture(0)
faceDetector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

detectFace(faceDetector, vid)

image = cv2.imread( 'Gray_Image.jpg', 1 );
cv2.imshow('frame',image);


print ("Face detection Begins...")