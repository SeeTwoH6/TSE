import cv2
import time
import numpy as np
import PoseModule as pm
import HandTrackingModule as htm
import mysql.connector

#The general idea is to take the 3 landmarks from the shoulder, elbow and wrist and calculate the angle between them to calculate whether a repetition has been completed


#Capture video camera code from https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/
cap = cv2.VideoCapture(0)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

#Test video
#cap = cv2.VideoCapture('PoseVideos/bicepReversed.mp4')

detector = pm.poseDetector()
handDetector = htm.HandDetector()
pTime = 0
exercise = "Shoulder Press" #Detect which exercise is being performed, default = Shoulder Press
reps = 0 #Count of how many repetitions of each exercise have been done
sets = 0 #Count of how many sets of each exercise have been done
totalReps = 0
direction = 0 #(0 is the concentric portion of the lift, 1 is the eccentric portion of the lift)
repCompleted = False
startExercise = False

count = 0
switch = True
modeChanged = False
startTime = 0

startDurationTimer = 0
duration = 0

def insertValues(exercise, sets, reps, duration):
    try:
        conn = mysql.connector.connect(
            host="192.168.149.185",
            user="27369364",
            password="27369364EC",
            database="healthapp"
        )
        cursor = conn.cursor()
        # Retrieves the new unique primary key identifier for the INSERT INTO query.
        query = "SELECT IFNULL((SELECT (MAX(ExerciseID) +1) FROM healthapp.Exercise), '1')"
        cursor.execute (query)
        exerciseID = cursor.fetchone()[0]
        print(f"Type of Exercise ID {type(exerciseID)}")
        query = "INSERT INTO Exercise (ExerciseID, ExerciseType, Duration, ExerciseUserID, Reps, Sets) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(query, (exerciseID, exercise, duration, 1, reps, sets))
        conn.commit()
        print(f"Added entry successfully, inserting: Ex ID: {exerciseID}, Type: {exercise}, Duration: {duration}, userID: {1}, reps: {reps}, sets: {sets}")
    except Exception as error:
        print(f"Database connection error: {error}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    #If flag == False, then the rest of the landmarks and lines are not drawn
    img = detector.findPose(img, False)
    lmList = detector.findPosePosition(img, False)

    img = handDetector.findHands(img)
    handLmList = handDetector.findHandPosition(img, draw = False)

    if len(handLmList) != 0:
        #Tip of index and middle fingers
        x1,y1 = handLmList[8][1:]
        x2,y2 = handLmList[12][1:]
        
        #Check which fingers are up
        fingers = handDetector.fingersUp()

        #Selection mode
        #1 fingers = Bicep Curls
        if fingers[1] and fingers[2] == False and fingers[3] == False and fingers[4] == False and fingers[0] == False:
            if exercise == "Bicep Curls":
                count = 0
                if count > 0:
                    switch = False
                else:
                    switch = True
            else:
                if count > 0:
                    switch = False
                else:
                    switch = True
                count += 1

            if switch:
                startTime = time.time()

            if startTime > 0:
                if time.time() - startTime > 2:
                    print("Switching to bicep curls")
                    startTime = 0
                    if startDurationTimer > 0:
                        duration = time.time() - startDurationTimer
                        startDurationTimer = 0
                        print(f"Duration: {duration}")
                        if totalReps > 0:
                            insertValues(exercise, sets, reps, duration)
                    exercise = "Bicep Curls"
                    totalReps = 0

        #2 fingers = Shoulder Press
        if fingers[1] and fingers[2] and fingers[3] == False and fingers[4] == False and fingers[0] == False:
            if exercise == "Shoulder Press":
                count = 0
                if count > 0:
                    switch = False
                else:
                    switch = True
            else:
                if count > 0:
                    switch = False
                else:
                    switch = True
                count += 1

            if switch:
                startTime = time.time()

            if startTime > 0:
                if time.time() - startTime > 2:
                    print("Switching to shoulder press")
                    startTime = 0
                    if startDurationTimer > 0:
                        duration = time.time() - startDurationTimer
                        startDurationTimer = 0
                        print(f"Duration: {duration}")
                        if totalReps > 0:
                            insertValues(exercise, sets, reps, duration)
                    exercise = "Shoulder Press"
                    totalReps = 0

        #3 fingers resets the exercise
        if (fingers[1] and fingers[2] and fingers[3] and fingers[4] == False and fingers[0] == False) or (fingers[2] and fingers[3] and fingers[4] and fingers[1] == False):
            if startExercise == False and (sets == 0 or reps == 0):
                count = 0
                if count > 0:
                    switch = False
                else:
                    switch = True
            else:
                if count > 0:
                    switch = False
                else:
                    switch = True
                count += 1

            if switch:
                startTime = time.time()

            if startTime > 0:
                if time.time() - startTime > 2:
                    print("Restarting")
                    startExercise = False
                    if startDurationTimer > 0:
                        duration = time.time() - startDurationTimer
                        startDurationTimer = 0
                        print(f"Duration: {duration}")
                        if totalReps > 0:
                            insertValues(exercise, sets, reps, duration)
                        
                    totalReps = 0

        #4 fingers starts the exercise
        if fingers[0] == False and fingers[1] and fingers[2] and fingers[3] and fingers[4]:
            if startExercise == True:
                count = 0
                if count > 0:
                    switch = False
                else:
                    switch = True
            else:
                if count > 0:
                    switch = False
                else:
                    switch = True
                count += 1

            if switch:
                startTime = time.time()
                if startDurationTimer == 0: #Starts the workout timer if it hasnt been started already
                    startDurationTimer = time.time()

            if startTime > 0:
                if time.time() - startTime > 2:
                    print("Starting exercise")
                    startExercise = True
                    startTime = 0

        #5 fingers stops the exercise
        if fingers[0] and fingers[1] and fingers[2] and fingers[3] and fingers[4]:
            if startExercise == False:
                count = 0
                if count > 0:
                    switch = False
                else:
                    switch = True
            else:
                if count > 0:
                    switch = False
                else:
                    switch = True
                count += 1



            if switch:
                startTime = time.time()

            if startTime > 0:
                if time.time() - startTime > 2:
                    print("Stopping exercise")
                    startExercise = False
                    startTime = 0

    if len(lmList) != 0:
        shoulderPressAngle = detector.findAngle(img, 13,11,23, False)
        #Right Arm
        rightArm = detector.findAngle(img, 12,14,16)
        #Left Arm
        leftArm = detector.findAngle(img, 11,13,15)

        #Handling whether the user is at the min and max point (percentage wise)
        #Range values for shoulder press
        if exercise == "Shoulder Press":
            bottomOfRep = 90
            topOfRep = 135
            per = np.interp(leftArm, (bottomOfRep, topOfRep), (0,100))
            #Create a bar to show the percentage of each rep completed
            #650 is the minimum of the bar, 100 is the maximum
            bar = np.interp(leftArm, (bottomOfRep, topOfRep), (650, 100))
        #Range values for bicep curls
        elif exercise == "Bicep Curls":
            if leftArm > 180:
                bottomOfRep = 210
                topOfRep = 310
                per = np.interp(leftArm, (bottomOfRep, topOfRep), (0,100))
                #Create a bar to show the percentage of each rep completed
                #650 is the minimum of the bar, 100 is the maximum
                bar = np.interp(leftArm, (bottomOfRep, topOfRep), (650, 100))
                
            if leftArm < 180:
                bottomOfRep = 150
                topOfRep = 50
                #Create a bar to show the percentage of each rep completed
                #650 is the minimum of the bar, 100 is the maximum
                per = np.interp(leftArm, (topOfRep, bottomOfRep), (100,0))
                bar = np.interp(leftArm, (topOfRep, bottomOfRep), (100, 650))



        #Check for each repetition
        if startExercise:
            if per == 100:
                if (exercise == "Shoulder Press" and shoulderPressAngle >= 140) or (exercise == "Bicep Curls"):
                    if direction == 0 and not repCompleted: #Concentric
                        repCompleted = True
                        totalReps += 1
                        direction = 1

            if per == 0:
                if direction == 1:
                    repCompleted = False
                    direction = 0

        
        sets = totalReps // 12
        reps = totalReps % 12
        #Print Sets
        cv2.putText(img, f'Sets: {int(sets)}', (45,600), cv2.FONT_HERSHEY_PLAIN, 7, (255,0,0), 10)
        #Present the reps on screen
        cv2.putText(img, f'Reps: {int(reps)} / 12', (45,700), cv2.FONT_HERSHEY_PLAIN, 7, (255,0,0), 10)

        #Print the bar on screen for left arm
        cv2.rectangle(img, (1100,100), (1175,650), (0,255,0), 3) 
        if leftArm < 180:
            cv2.rectangle(img, (1100,int(bar)), (1175,650), (0,255,0), cv2.FILLED) 
        elif leftArm > 180:
            cv2.rectangle(img, (1100,int(bar)), (1175,650), (0,255,0), cv2.FILLED) 
        cv2.putText(img, f'{int(per)}%', (1100,75), cv2.FONT_HERSHEY_PLAIN, 4, (255,0,0), 4)

        #Print exercise being performed
        cv2.putText(img, f'Exercise: {exercise}', (40,90), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0), 5)

        #Print whether the program will start counting their exercise
        cv2.putText(img, f'Start Count? {startExercise}', (40,150), cv2.FONT_HERSHEY_PLAIN, 4, (255,0,0), 5)

        #Adding FPS Counter
        cTime = time.time()
        fps = int(1/(cTime-pTime))
        pTime = cTime
        cv2.putText(img, f'FPS: {fps}', (40,210), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 5)


    #Prints image
    cv2.imshow("Image", img)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break
