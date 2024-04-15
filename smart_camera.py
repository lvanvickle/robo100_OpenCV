import cv2
import sys

# Create an object of the class CascadeClassifier
# with the Haar Cascade XML file that has been trained
# to detect the front of faces.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize video capture with the default webcam.
# '0' refers to the first camera connected to the computer.
cap = cv2.VideoCapture(0)

while True:
    # Read each frame from the camera.
    # read() returns a bool value if the read is successful
    # and the frame it captured.
    # The bool value is saved to "_" and the frame is
    # saved to "img."
    _, img = cap.read()
    
    # Convert to grayscale.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Display
    cv2.imshow('img', img)
    
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
