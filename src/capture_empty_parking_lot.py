# Importing the necessary Python libraries
import cv2

# Starting the video capture from USB webcam
webcam_capture = cv2.VideoCapture(0)

# Capturing the current frame from the webcam
# (Note: You will often see that "webcam_connection_bool" as "ret" in other examples)
webcam_connection_bool, frame = webcam_capture.read()

# Saving the frame as a JPEG to our data/ directory
cv2.imwrite('../data/empty_parking_lot.jpeg', frame)

# Properly halting video and video display window
webcam_capture.release()
cv2.destroyAllWindows()