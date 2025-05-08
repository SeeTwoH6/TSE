import cv2
import mediapipe as mp
import time

#Most of the code is taken from https://www.youtube.com/watch?v=01sAkU_NvOY&t=668s

class HandDetector():
    def __init__(self, mode = False, maxHands = 2, modelComplexity = 1, detectCon = 0.94, trackCon = 0.75):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectCon = detectCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity, self.detectCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

        self.tipIds = [4,8,12,16,20]

    def findHands(self, img, draw = True):
        #Check for detection
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.handResults = self.hands.process(imgRGB)
        if self.handResults.multi_hand_landmarks:
            for handLms in self.handResults.multi_hand_landmarks:
                #Get thumb and pinky x coordinates
                thumb_x = handLms.landmark[4].x
                pinky_x = handLms.landmark[20].x

                #If thumb_x > pinky_x, then it must be the right hand
                if thumb_x > pinky_x:
                    if draw:
                        self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                    break #Only process the first right hand detected
        return img

    def findHandPosition(self, img, handNo=0, draw = True):
        self.lmList = []
        if self.handResults.multi_hand_landmarks:
            for handNo, hand in enumerate(self.handResults.multi_hand_landmarks):
                thumb_x = hand.landmark[4].x
                pinky_x = hand.landmark[20].x

                if thumb_x > pinky_x:
                    #Get id number and landmark info for each hand
                    for id, lm in enumerate(hand.landmark):
                        height, width, channel = img.shape
                        cx, cy = int(lm.x * width), int(lm.y * height)
                        self.lmList.append([id, cx, cy])
                        if draw:
                            cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)
                    break #Only process the first right hand detected
        return self.lmList
    
    def fingersUp(self):
        fingers = []

        #Thumb
        #Check if the thumb is on the left or right hand
        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        #Check if each of the four fingers are above/below the landmark two below it
        #If above, then the finger is up, else it is down
        for id in range(1,5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

def main():
    pass

if __name__ == "__main__":
    main()