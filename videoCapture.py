import cv2 

video = cv2.VideoCapture(0)

while True:
    success, frame = video.read()
    
    cv2.imshow("frame", frame)
    cv2.waitKey(1)
    
