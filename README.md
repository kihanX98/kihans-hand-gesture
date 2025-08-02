# Tekken Motion Control System 🎮🕹️

Control Tekken using your body movements — no controller needed! This project uses your webcam to detect body gestures and map them to game controls in real-time.

## 💡 Overview
This project lets players control a fighting game like **Tekken** using full-body gestures detected through a standard webcam. It leverages **MediaPipe** for pose tracking and **PyAutoGUI** for simulating keyboard inputs.

## 🧠 How It Works
Using **MediaPipe Pose**, the program detects the position of your hands, shoulders, and nose. Based on their positions, it triggers keyboard events to perform in-game actions.

### 🤸 Gesture Mappings:
- 🙌 **Both Hands Up (above head)** → `Jump` (presses `Space`)
- 🛡️ **Both Hands Near Chest (defense pose)** → `Defend` (presses `Down`)
- 👊 **Left Hand Up (right hand down)** → `Punch` (presses `Z`)
- 🦵 **Right Hand Up (left hand down)** → `Kick` (presses `X`)

## 🧰 Requirements
- Python 3.12
- OpenCV (`opencv-python`)
- MediaPipe (`mediapipe`)
- PyAutoGUI (`pyautogui`)

Install them with:
```bash
pip install opencv-python mediapipe pyautogui
🚀 How to Run
bash
Copy
Edit
python pose_test.py
Make sure your webcam is on.

Stand in frame and try different gestures.

Press q to quit the app.
🎮 Game Compatibility
This is tested with games that support keyboard controls. It works best with emulators or PC games where you can map actions to keys (Space, Z, X, Down). It does not directly connect to Tekken or other paid games.

📌 Note
You must open the game and keep the focus on it while running the script so that PyAutoGUI inputs are registered.
