import cv2
def read_cam():
    cap = cv2.VideoCapture("v4l2src device=/dev/video0 ! video/x-raw, width=640, height=480 ! videoconvert ! video/x-raw,format=BGR ! appsink")
    if cap.isOpened():
        cv2.namedWindow("demo", cv2.WINDOW_AUTOSIZE)
        while True:
            ret_val, frame = cap.read()
            cv2.imshow('demo', frame)
            cv2.waitKey(10)

            result, _, _ = cv2.QRCodeDetector().detectAndDecode(frame)
            if result:
                print result
    else:
        print "camera open failed"

    cv2.destroyAllWindows()


if __name__ == '__main__':
    read_cam()
