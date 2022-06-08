import cv2

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    _, image = cap.read()
    res, _, image2 = detector.detectAndDecode(image)
    if res:
        print(type(res))
        cv2.imshow("Video1", image2)
    cv2.imshow("Video", image)
    cv2.waitKey(1)
