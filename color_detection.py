import numpy as np
import cv2

img = cv2.imread("rubix.jpeg")


hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


red_lower = np.array([136, 87, 111], np.uint8)
red_upper = np.array([180, 255, 255], np.uint8)
red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

green_lower = np.array([40, 40, 40], np.uint8)
green_upper = np.array([70, 255, 255], np.uint8)
green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)


blue_lower = np.array([94, 80, 2], np.uint8)
blue_upper = np.array([120, 255, 255], np.uint8)
blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

yellow_lower = np.array([20, 100, 100], np.uint8)
yellow_upper = np.array([30, 150, 255], np.uint8)
yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)

orange_lower = np.array([10, 100, 20], np.uint8)
orange_upper = np.array([25, 255, 255], np.uint8)
orange_mask = cv2.inRange(hsvFrame, orange_lower, orange_upper)

white_lower = np.array([0, 0, 0], np.uint8)
white_upper = np.array([20, 25, 225], np.uint8)
white_mask = cv2.inRange(hsvFrame, white_lower, white_upper)


kernal = np.ones((5, 5), "uint8")

# For red color
red_mask = cv2.dilate(red_mask, kernal)
res_red = cv2.bitwise_and(img, img, mask=red_mask)

# For green color
green_mask = cv2.dilate(green_mask, kernal)
res_green = cv2.bitwise_and(img, img, mask=green_mask)

# For blue color
blue_mask = cv2.dilate(blue_mask, kernal)
res_blue = cv2.bitwise_and(img, img, mask=blue_mask)
# Yellow
yellow_mask = cv2.dilate(yellow_mask, kernal)
res_yellow = cv2.bitwise_and(img, img, mask=yellow_mask)

# orange
orange_mask = cv2.dilate(orange_mask, kernal)
res_orange = cv2.bitwise_and(img, img, mask=orange_mask)

# White
white_mask = cv2.dilate(white_mask, kernal)
res_white = cv2.bitwise_and(img, img, mask=white_mask)

# Creating contour to track red color
contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if area > 300:
        x, y, w, h = cv2.boundingRect(contour)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.putText(img, "Red", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))

# contour for yellow
contours, hierarchy = cv2.findContours(
    yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)


for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if area > 1000:
        x, y, w, h = cv2.boundingRect(contour)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

        cv2.putText(img, "Yellow", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255))

# contour for green
contours, hierarchy = cv2.findContours(
    green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)

for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if area > 300:
        x, y, w, h = cv2.boundingRect(contour)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.putText(img, "Green", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))

# contour for blue
contours, hierarchy = cv2.findContours(
    blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)
for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if area > 1000:
        x, y, w, h = cv2.boundingRect(contour)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.putText(img, "Blue", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))

# contour for orange
contours, hierarchy = cv2.findContours(
    orange_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)
for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if area > 1000:
        x, y, w, h = cv2.boundingRect(contour)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 140, 255), 2)

        cv2.putText(img, "Orange", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 140, 255))

# white contour
contours, hierarchy = cv2.findContours(
    white_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)
for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if 1500 < area < 44600:
        x, y, w, h = cv2.boundingRect(contour)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)

        cv2.putText(img, "White", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0))

cv2.imshow("TILES", img)

key = cv2.waitKey(0)

cv2.destroyAllWindows()
