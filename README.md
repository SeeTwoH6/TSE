Opening app and running tests 

To open the app or use a test on it use these command 

Python main.py - To run the application 

Python –m unittest testing.py - to test the application 

 

Main menu 

Picture 

 

This is the home page of the application, if you click on one of these buttons it will take you to that activity and you can input what you have done. Below is a list of things to the buttons and menu do 

Cognitive exercises – will take you to a menu of cognitive exercises you can do 

Calorie Intake – will take you to the calorie page  

Water Intake – will take you to the water Intake page 

Exercise Activity – will take you an exercise activity page 

Menu will list do the same thing as the buttons but will list out all the options 

 

Cognitive Exercises 

Picture 

This is the menu for the cognitive exercises page. There are 4 buttons dedicated to the 4 cognitive exercises that can be completed. Here are what the 4 buttons do 

Counting Exercise – launches the counting game  

Balencing Exercise – launches balancing game 

Memory Exercise – launches Memory game 

Reaction Exercise – launches reaction game 

Water Intake menu 

Picture 

This would take an input from the amount of water the user drank, and it will be submitted. It would then update the glass showing the amount of water the user has drank and if they have reached the limit of what an average human drink 

Features: 

Total intake – shows the total intake of water the user has drank 

Input box - takes the water intake input from the box. 

Submit button - submits them into the box to tell and adds it too the total water intake 

Cup and water – the amount of water the user has drank is represented by a cup and water filling up in the cup each time 

 

Calorie intake 

 

Picture 

 

 

 

This is the calorie intake GUI, this will take in what the user has consumed for either, breakfast, lunch, dinner or snack and it will output it in the table 

Features: 

Pie Chart – the pie chart will output the nutrients that the user has consumed over the day.  

Breakfast, Lunch, dinner, snack – launches the food list UI 

Food list GUI 

Picture 

 

This will allow the user to select a food from this list and then update the pie chart with what they consumed.  

Food List box – shows a list of foods 

Confirm button- will add the nutrients from the selected list box and adds up the total amount of carbs, fat and protein the user has consumed 

 

 

 

Counting Game- In this game the user gets asked how many blocks there are on the screen, whilst being timed. The game starts off easy with blocks only being shown on a 2D plane, but they then increase after each round, and the user can also play on a 3D plane which will take them more time. 

 

Memory Game – The memory game starts off with the user being shown 4 numbers in a 4x4 grid, with the user being flashed those numbers for 3 seconds, after that the numbers disappear and the grid is just empty with blocks, the player has to sequentially press the blocks in order to then get a score, one correct press equals one score. After each round is complete the number increases by 1, adding more challenge to the game, if the user gets it wrong the game ends.  

 

Reaction Game- The person presses on the screen and the game will start, at any random point the screen will change colour is when you will need to press to see how fast you reacted.  

 

Computer Vision – AIBodyTracker 

This program works by identifying the body’s wrist, elbow, shoulder and hip and calculating the angles to determine how many repetitions of each exercise the user performs. Please ensure that the user is always in full view of the camera for accurate tracking and time recording. Shoulder presses are only calculated if the arms are positioned at the correct angle. Repetitions are only counted on the user’s left arm. 

The user can use hand gestures to control the program 

Hand Gesture Controls 

The program detects the user’s right hand by identifying which side the pinkie is on in relation to the thumb. Controls are dictated by the number of fingers the user holds up. 

1 Finger – Switches the exercise to bicep curls 

2 Fingers – Switches the exercise to shoulder press 

3 Fingers – Resets the workout by stopping to record the workout and resetting the reps and sets to 0 

4 Fingers – Starts the workout 

5 Fingers – Temporarily Pauses the workout 

Fingers must be held up for 2 seconds before the modes switch. Press ‘q’ to quit the program 

 

 
