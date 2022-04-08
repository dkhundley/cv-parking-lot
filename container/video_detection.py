# Importing the required Python libraries
import cv2

# Instantiating the object for the video capture here
video_stream = cv2.VideoCapture(1)

while True:
    ret, frame = video_stream.read()

    if ret is False:
        break

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1) &0xFF
    if key == ord('q'):
        break