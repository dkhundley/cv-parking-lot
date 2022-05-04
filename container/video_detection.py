# Importing the required Python libraries
import cv2

## SCRIPT INSTANTIATION
## ---------------------------------------------------------------------------------------------------------------------
# Instantiating the object for the video capture here
video_stream = cv2.VideoCapture(1)

# Loading the vehicle detection model
vehicle_detection_model = cv2.CascadeClassifier('../models/vehicle-detection-model.xml')

# Printing statement indicating proper way to halt video capture manually
print('Starting video stream! To halt stream, please press the \"q\" key on your keyboard.')



## ONGOING VIDEO CAPTURE STREAM
## ---------------------------------------------------------------------------------------------------------------------
# Continuing to iterate through the individual frames of video capture until manually stopped
while True:

    # Retrieving the individual frame from the video capture
    ret, frame = video_stream.read()

    # Halting the stream if something is not technically working
    if (ret is False) or (type(frame) == type(None)):
        break

    # Turning the frame into a grayscale image
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Getting all detected vehicles from the frame with the vehicle detection model
    all_vehicles = vehicle_detection_model.detectMultiScale(grayscale_frame, 1.1, 2)

    # Drawing a bounding box around all detected vehicles
    for (x, y, w, h) in all_vehicles:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), 2)

    # Showing the current frame with appropriate bounding boxes
    cv2.imshow('frame', frame)

    # Setting the breaking key to halt the video capture when manually triggered
    if cv2.waitKey(1) == ord('q'):
        break