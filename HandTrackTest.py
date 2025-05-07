import time
import cv2
import mediapipe as mp
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)

detector = htm.HandDetector()

while True:
    success,img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findHandPosition(img, draw = False)
    if len(lmList) != 0:
        print(lmList[4])



    cv2.imshow("Image", img)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break