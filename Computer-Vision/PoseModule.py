import cv2 #Library for image processing
import mediapipe as mp #Framework for code estimation
import time
import math

#Most of the code is taken from https://www.youtube.com/watch?v=01sAkU_NvOY&t=668s

#Create class to instantiate objects that have methods that will detect poses and find all the landmarks
class poseDetector():
    #Changed the init from the video the code is referenced from due to updates to the Pose() class
    def __init__(self, mode=False, modelComplexity = 1, smoothLandmarks = True, enableSegment = False, smoothSegment = True, detectionCon = 0.5, trackingCon=0.5):
        self.mode = mode
        self.modelComplexity = modelComplexity
        self.smoothLandmarks = smoothLandmarks
        self.enableSegment = enableSegment
        self.smoothSegment = smoothSegment
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        #Pose() takes static image mode to detect whether detection or tracking is taking place
        #When true, tries to detect, else tracks if the confidence is high
        #If detection conf > 0.5 then checks tracking conf > 0.5. If tracking conf > 0.5 then keep tracking. When < 0.5, goes back to detection conf
        self.pose = self.mpPose.Pose(mode, modelComplexity, smoothLandmarks, enableSegment, smoothSegment, detectionCon, trackingCon)

        

    def findPose(self, img, draw=True):
        #Mediapipe uses RBG but img uses BGR, so this line harmonises the two by converting to RGB 
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        #Draw
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return img

    def findPosePosition(self, img, draw=True):
        self.lmList = []
        #If the results are available
        if self.results.pose_landmarks:
            #Organising landmarks by looping through the id and landmarks
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                #Height, width and channel
                height, width, channel = img.shape
                #print(id, lm)
                #So far the landmarks show a ratio of the image
                #To get pixel value,
                cx, cy = int(lm.x*width), int(lm.y*height)
                self.lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx,cy), 10, (255,0,0), cv2.FILLED)
        return self.lmList
    
    def findAngle(self, img, p1, p2, p3, draw = True):
        #Fetch the landmark of interest and store its x and y coordinates, slicing off the first element which holds the landmark of interest
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        #Calculate the angle
        angle = math.degrees(math.atan2(y3-y2,x3-x2) - math.atan2(y1-y2,x1-x2))

        #Correcting if angle is less than 0 degrees
        if angle < 0:
            angle += 360
        #Draw
        if draw:
            #Highlighting the landmarks of interest
            cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 3)
            cv2.line(img, (x3,y3), (x2,y2), (0,255,0), 3)
            cv2.circle(img, (x1,y1), 10, (0,0,255), cv2.FILLED)
            cv2.circle(img, (x1,y1), 15, (0,0,255), 2)
            cv2.circle(img, (x2,y2), 10, (0,0,255), cv2.FILLED)
            cv2.circle(img, (x2,y2), 15, (0,0,255), 2)
            cv2.circle(img, (x3,y3), 10, (0,0,255), cv2.FILLED)
            cv2.circle(img, (x3,y3), 15, (0,0,255), 2)

            #Display angle
            #cv2.putText(img, str(int(angle)), (x2-50, y2+50), cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2)
        return angle


def main():
    pass

if __name__ == "__main__":
    main()