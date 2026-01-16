import cv2
from ultralytics import YOLO

# awakening of the Brain

model = YOLO("yolov8n.pt") #its also called as weights : here all the training is stored

# starting the webcam (openig the eyes)

cap = cv2.VideoCapture(0) # i have written 0 for the camera, if i would had a external camera then maybe i would have written "1" etc.

while True:
    ret, frame = cap.read() # this means take a photo(a frame) from the camera
    results = model(frame) # to check the photo
    annotated_frame = results[0].plot() # make a kind of a box on the photo(frame).
    cv2.imshow("My Project", annotated_frame) #show it on the new screen.

    if cv2.waitKey(1) == ord("q"): # if i will press q then stop the running program.
        break
