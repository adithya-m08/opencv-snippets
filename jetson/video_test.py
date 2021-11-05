import cv2

cap = cv2.VideoCapture(
    "v4l2src device=/dev/video0 ! video/x-raw, width=640, height=480 ! videoconvert ! video/x-raw,format=BGR ! appsink"
)
while True:
    _, frame = cap.read()
    cv2.imshow("Frame", frame)
    if cv2.waitKey(5) & 0xFF != ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
