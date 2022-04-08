# Importing the necessary Python libraries
import cv2
import time
import numpy as np
import imutils
from imutils.video import VideoStream
from imutils.video import FPS



## ENVIRONMENT INSTANTIATION
## ---------------------------------------------------------------------------------------------------------------------
# Denoting the 21 class types that MobileNet SSD is trained to view
CLASSES = ['aeroplane', 'background', 'bicycle', 'bird', 'boat',
           'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable',
           'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep',
           'sofa', 'train', 'tvmonitor']

# Assigning random colors to each of the classes
COLORS = np.random.uniform(0, 255, size = (len(CLASSES), 3))

# Loading the model from files
model = cv2.dnn.readNetFromCaffe(prototxt = 'models/MobileNetSSD_deploy.prototxt.txt',
                                 caffeModel = 'models/MobileNetSSD_deploy.caffemodel')



## VIDEO STREAM
## ---------------------------------------------------------------------------------------------------------------------
# Starting the video stream
stream = VideoStream(src = 1).start()
time.sleep(2.0)

# Starting the FPS timer
fps = FPS().start()

# Continuing to iterate over frames while video stream remains alive
while True:

    # Analyzing the current frame
    current_frame = stream.read()
    current_frame = imutils.resize(current_frame, width = 400)
    print(current_frame.shape)

    (height, width) = current_frame.shape[:2]

    resized_image = cv2.resize(current_frame, (500, 500))

    blob = cv2.dnn.blobFromImage(resized_image, (1/127.5), (500, 500), 127.5, swapRB = True)

    model.setInput(blob)

    predictions = model.forward()

    # Iterating over all the predictions
    for i in np.arange(0, predictions.shape[2]):
        confidence = predictions[0, 0, i, 2]
        if confidence > 0.2:
            idx = int(predictions[0, 0, i, 1])
            box = predictions[0, 0, i, 3:7] * np.array([width, height, width, height])
            (x_start, y_start, x_end, y_end) = box.astype("int")
            label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
            cv2.rectangle(current_frame, (x_start, y_start), (x_end, y_end), COLORS[idx], 2)
            y = y_start - 15 if y_start - 15 > 15 else y_start + 15
            cv2.putText(current_frame, label, (x_start, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

    # Showing the outputted frame
    cv2.imshow("Frame", current_frame)

    # Press 'q' key to break the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

    # update the FPS counter
    fps.update()

# Stopping the timer
fps.stop()
cv2.destroyAllWindows()
vs.stop()