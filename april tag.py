import cv2
import apriltag

cap=cv2.VideoCapture(0)

while True:
    ret_val, img = cap.read();
    cv2.imshow('Apriltag',img)
    cv2.waitKey(1)
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    result = apriltag.Detector().detect(img_gray)
    if result:
        print(result[0][1])