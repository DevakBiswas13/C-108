from operator import index
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips =[8, 12, 16, 20]
thumb_tip= 4

while True:
    ret,img = cap.read()
    img = cv2.flip(img, 1)
    h,w,c = img.shape
    results = hands.process(img)


    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            if hand_landmark:
                landmarks = hand_landmark[hands].landmark
                print(landmarks)
            #accessing the landmarks by their position
                lm_list=[]
                fingertipY = results[index].y
                fingerbottomY = results[finger_tips-2].y
                if fingerbottomY > fingertipY:
                    lm_list.append(lm)
                    print("Thumb is down :(")
                if fingertipY > fingerbottomY:
                    lm_list.append(0)
                    print("Thumbs Up :)")
        total_finger = fingers.count(1)
        text = f'Fingers: {total_finger}'
        cv2.putText(img, text, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2) 
                

            



        mp_draw.draw_landmarks(img, hand_landmark,
        mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0,0,255),2,2),
        mp_draw.DrawingSpec((0,255,0),4,2))
    

    cv2.imshow("hand tracking", img)
    cv2.waitKey(1)

    