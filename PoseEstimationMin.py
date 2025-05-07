import cv2 #Library for image processing
import mediapipe as mp #Framework for code estimation
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
#Pose() takes static image mode to detect whether detection or tracking is taking place
#When true, tries to detect, else tracks if the confidence is high
#If detection conf > 0.5 then checks tracking conf > 0.5. If tracking conf > 0.5 then keep tracking. When < 0.5, goes back to detection conf
pose = mpPose.Pose()
cap = cv2.VideoCapture('PoseVideos/dance.mp4')
pTime = 0
while True:
    sucess, img = cap.read()
    #Mediapipe uses RBG but img uses BGR, so this line harmonises the two by converting to RGB 
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    #Draw
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        #Organising landmarks by looping through the id and landmarks
        for id, lm in enumerate(results.pose_landmarks.landmark):
            #Height, width and channel
            height, width, channel = img.shape
            print(id, lm)
            #So far the landmarks show a ratio of the image
            #To get pixel value,
            cx, cy = int(lm.x*width), int(lm.y*height)
            cv2.circle(img, (cx,cy), 10, (0,0,255), cv2.FILLED)



    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)
    resizedImg = cv2.resize(img, (1280, 720))
    cv2.imshow("Image", resizedImg)
    cv2.waitKey(1)

