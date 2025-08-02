import cv2
import mediapipe as mp
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Start camera
cap = cv2.VideoCapture(0)

# Initialize Pose model
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Ignoring empty camera frame.")
            continue

        # Flip and convert to RGB
        image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)

        # Convert back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark

            # Get landmarks
            left_hand = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]
            right_hand = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]
            left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
            right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
            nose = landmarks[mp_pose.PoseLandmark.NOSE]

            lh_y = left_hand.y
            rh_y = right_hand.y
            ls_y = left_shoulder.y
            rs_y = right_shoulder.y
            nose_y = nose.y

            # Detect Jump (both hands above head)
            if lh_y < nose_y and rh_y < nose_y:
                pyautogui.press('space')
                print("Jump")

            # Detect Defend (both hands below shoulders)
            elif lh_y > ls_y and rh_y > rs_y:
                pyautogui.press('down')
                print("Defend")

            # Detect Punch (left hand raised)
            elif lh_y < ls_y and rh_y > rs_y:
                pyautogui.press('z')
                print("Punch")

            # Detect Kick (right hand raised)
            elif rh_y < rs_y and lh_y > ls_y:
                pyautogui.press('x')
                print("Kick")

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        cv2.imshow('Tekken Motion Controller', image)

        # Press 'q' to quit
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()


