# AI Hand Gesture Controller

An AI-powered hand gesture controller built using Python, OpenCV, and MediaPipe. The application detects hand gestures in real time through a webcam and performs different system actions such as opening applications, taking screenshots, and controlling the system volume.

## Features

- Real-time hand detection and tracking
- Gesture recognition using MediaPipe
- Launch desktop applications
- Take screenshots
- Control system volume
- Live webcam preview with detected gesture
- Action cooldown to prevent repeated execution

## Technologies Used

- Python 3.10+
- OpenCV
- MediaPipe 0.10.14
- PyAutoGUI

## Project Structure

```
Handgesture/
│
├── gesture_controller.py
├── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Roshan3724/Handgesture.git
```

Move into the project folder:

```bash
cd Handgesture
```

Install the required packages:

```bash
pip install opencv-python mediapipe==0.10.14 pyautogui
```

## Running the Project

```bash
python gesture_controller.py
```

## Gesture Controls

| Gesture | Action |
|----------|--------|
| ✊ Fist | Open Notepad |
| 👍 Thumbs Up | Open Google Chrome |
| ☝️ One Finger | Open Calculator |
| ✌️ Peace Sign | Open Visual Studio Code |
| 🖐 Open Palm | Take Screenshot |
| 🤟 Rock Sign | Increase Volume |
| 🤙 Thumb + Pinky | Decrease Volume |

> **Note:** Make sure each gesture is unique to avoid conflicts during detection.

## How It Works

1. Opens the webcam.
2. Detects the user's hand using MediaPipe.
3. Recognizes the current hand gesture.
4. Matches the gesture with a predefined action.
5. Executes the corresponding system command.
6. Displays the detected gesture on the screen.

## Output

The application displays:

- Live webcam feed
- Hand landmarks
- Detected gesture name
- Executed system action

## Requirements

- Windows 10/11
- Python 3.10 or later
- Working webcam

## Future Improvements

- Finger counting
- Virtual mouse control
- Air drawing
- Presentation controller
- Music controller
- Custom gesture mapping
- Face recognition integration
- Graphical user interface (GUI)

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

## License

This project is licensed under the MIT License.

## Author

**Roshan Khatiwada**

GitHub: https://github.com/Roshan3724

## Acknowledgements

- OpenCV
- MediaPipe
- PyAutoGUI