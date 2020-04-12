#Import OpenCV
import cv2
#Import Face recognition
import face_recognition

video_capture = cv2.VideoCapture(0)
#Initializing to empty list
face_locations = [] 

while True:
    ret, frame = video_capture.read()
    #Converting the video from BGR to RGB
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame,(left, top), (right, bottom), (0, 0, 255), 2)
        cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


