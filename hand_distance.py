import cv2
from hand_tracking import handDetector
import math
import numpy as np

# Webcam
cap = cv2.VideoCapture(0)

# Hand Detector
detector = handDetector(detectionCon=0.5, maxHands=1)

# Find Function
# x is the raw distance y is the value in cm
x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
coff = np.polyfit(x, y, 2)  # y = Ax^2 + Bx + C

# Loop
while True:
    success, img = cap.read()
    hands = detector.findHands(img, draw=True)

    if hands.any():
        print(hands)
        # lmList = hands[0]["lmList"]
        # x, y, w, h = hands[0]["bbox"]
        # x1, y1 = lmList[5]
        # x2, y2 = lmList[17]

        # distance = int(math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))
        # A, B, C = coff
        # distanceCM = A * distance ** 2 + B * distance + C

        # # print(distanceCM, distance)

        # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)
        # cv2.putTextRect(img, f"{int(distanceCM)} cm", (x + 5, y - 10))

    cv2.imshow("Image", img)
    cv2.waitKey(1)
