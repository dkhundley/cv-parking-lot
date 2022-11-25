# Importing the necessary Python libraries
import cv2

# Starting the video capture from USB webcam
webcam_capture = cv2.VideoCapture(0)

# Continuing to iterate over video until manually stopped
while True:

    # Capturing the current frame from the webcam
    # (Note: You will often see that "webcam_connection_bool" as "ret" in other examples)
    webcam_connection_bool, frame = webcam_capture.read()

    # Displaying the frame if CV2 can properly detect the camera
    if webcam_connection_bool:
        cv2.imshow('My Webcam Video', frame)

    # Waiting for human input to stop the video by pressing the 'q' key on the keyboard
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Properly halting video and video display window
webcam_capture.release()
cv2.destroyAllWindows()