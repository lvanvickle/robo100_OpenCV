import cv2

# Initialize video capture with the default webcam.
# '0' refers to the first camera connected to the computer.
cap = cv2.VideoCapture(0)

# Check to see if the camera was initialized successfully.
if not cap.isOpened():
    print("Cannot open camera")
    exit()
# Attempt to read frame from camera
ret, frame = cap.read()
if not ret:
    print("Can't receive frame (stream end?). Exiting ...")
    cap.release()
    exit()
# Display the frame
cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
