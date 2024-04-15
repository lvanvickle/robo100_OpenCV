import cv2
cap = cv2.VideoCapture(0) # 0 is usually the default ID for the first capera.

if not cap.isOpened():
    print("Cannot open camera")
    exit()
ret, frame = cap.read()
if not ret:
    print("Can't receive frame (stream end?). Exiting ...")
    cap.release()
    exit()
cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
