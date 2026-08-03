import cv2
import mediapipe as mp
import pyautogui
import os
import time

# -----------------------------
# MediaPipe Setup
# -----------------------------
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# -----------------------------
# Webcam Setup
# -----------------------------
cap = cv2.VideoCapture(0)

# Prevent repeated actions
last_action_time = 0
ACTION_DELAY = 2

# -----------------------------
# Count Fingers Function
# -----------------------------
def count_fingers(hand_landmarks):
    tip_ids = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb
    if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for i in range(1, 5):
        if hand_landmarks.landmark[tip_ids[i]].y < hand_landmarks.landmark[tip_ids[i] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

# -----------------------------
# Detect Gesture
# -----------------------------
def detect_gesture(fingers):
    total = fingers.count(1)

    if fingers == [0, 0, 0, 0, 0]:
        return "FIST"

    elif fingers == [1, 0, 0, 0, 0]:
        return "THUMBS UP"

    elif fingers == [0, 1, 1, 0, 0]:
        return "PEACE"

    elif fingers == [0, 1, 0, 0, 0]:
        return "ONE FINGER"

    elif fingers == [0, 1, 1, 1, 1]:
        return "OPEN PALM"

    elif total == 2:
        return "TWO FINGERS"

    elif total == 3:
        return "THREE FINGERS"

    return "UNKNOWN"

# -----------------------------
# Perform Action
# -----------------------------
def perform_action(gesture):
    global last_action_time

    current_time = time.time()

    if current_time - last_action_time < ACTION_DELAY:
        return

    if gesture == "THUMBS UP":
        print("Opening Chrome...")
        os.system("start chrome")

    elif gesture == "PEACE":
        print("Opening VS Code...")
        os.system("code")

    elif gesture == "FIST":
        print("Opening Notepad...")
        os.system("notepad")

    elif gesture == "ONE FINGER":
        print("Opening Calculator...")
        os.system("calc")

    elif gesture == "OPEN PALM":
        filename = f"screenshot_{int(current_time)}.png"
        pyautogui.screenshot(filename)
        print(f"Screenshot saved: {filename}")

    elif gesture == "TWO FINGERS":
        pyautogui.press("volumeup")
        print("Volume Up")

    elif gesture == "THREE FINGERS":
        pyautogui.press("volumedown")
        print("Volume Down")

    last_action_time = current_time
    
    # -----------------------------
# Main Loop
# -----------------------------
while True:
    success, frame = cap.read()

    if not success:
        print("Failed to access camera")
        break

    # Mirror image
    frame = cv2.flip(frame, 1)

    # Convert to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process hand detection
    result = hands.process(rgb)

    gesture_name = "NO HAND"

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:

            # Draw landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3),
                mp_draw.DrawingSpec(color=(255, 0, 0), thickness=2)
            )

            # Count fingers
            fingers = count_fingers(hand_landmarks)

            # Detect gesture
            gesture_name = detect_gesture(fingers)

            # Perform action
            perform_action(gesture_name)

    # Display gesture
    cv2.rectangle(frame, (10, 10), (350, 80), (0, 0, 0), -1)

    cv2.putText(
        frame,
        f"Gesture: {gesture_name}",
        (20, 55),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    # Instructions
    cv2.putText(frame, "ESC = Exit", (20, 470),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("AI Hand Gesture Controller", frame)

    # Exit with ESC key
    if cv2.waitKey(1) == 27:
        break

# -----------------------------
# Cleanup
# -----------------------------
cap.release()
cv2.destroyAllWindows()