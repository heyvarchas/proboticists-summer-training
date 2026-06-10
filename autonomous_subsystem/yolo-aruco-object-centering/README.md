# Project Title

Real-time object centering using YOLOv8 for target detection and ArUco markers for reference frame estimation.

---

# Overview

This project detects a target object in a live camera feed, finds the center of a reference frame built from four ArUco markers, and compares the two centers to guide the user on how to move the object until it is centered. In the current implementation, the target object is a water bottle, and the reference frame is defined by ArUco markers with IDs `0, 1, 2, 3`.

---

# Features

- Real-time webcam/video-stream processing with OpenCV.
- YOLOv8-based object detection for the target class (`bottle`).
- ArUco marker detection using the `DICT_4X4_50` dictionary.
- Automatic computation of the object center and frame center.
- Visual annotations for debugging and demonstration:
  - blue bounding box and center dot for the detected bottle,
  - green dots for individual ArUco marker centers,
  - red dot for the computed frame center,
  - yellow line connecting the object center and frame center.
- Direction guidance based on horizontal and vertical offsets.
- Threshold-based “CENTERED” state to avoid noisy movement instructions.

---

# System Workflow

1. Capture frames from the camera.
2. Run YOLO on every frame and look for the target object.
3. Detect ArUco markers in the same frame.
4. Compute the center of each detected marker.
5. When markers `0, 1, 2, 3` are all present, compute the frame center as the average of their centers.
6. Compute `dx` and `dy` between the object center and the frame center.
7. Use the offset values and a threshold to decide whether the object should move left, right, up, down, or is already centered.
8. Display the final annotated frame in a window.

---

# Demo

The repository includes sample visuals and a demonstration video that show the system in action:

- `Object_Center_Detection.png`
- `Frame_Center_Detection.png`
- `Project_Demonstration.mp4`

These assets show the object center detection, frame center detection, and the final centering workflow.

---

# Hardware Requirements

- A laptop or desktop computer.
- A camera input source:
  - USB webcam, or
  - phone camera used as a webcam through DroidCam.
- Printed ArUco markers for IDs `0, 1, 2, 3`.
- A target object to detect and center, such as a water bottle.

---

# Software Requirements

- Python 3.x
- OpenCV with ArUco support (`opencv-contrib-python`)
- Ultralytics YOLO

Recommended environment:

- `cv2`
- `ultralytics`

---

# Project Structure

```text
.
├── main.py
├── Documentation.ipynb
├── Project_Demonstration.mp4
├── Object_Center_Detection.png
├── Frame_Center_Detection.png
├── marker_0.png
├── marker_1.png
├── marker_2.png
├── marker_3.png
└── README.md
```

- `main.py` contains the live detection and centering logic.
- `Documentation.ipynb` contains the step-by-step development notes and testing workflow.
- `Project_Demonstration.mp4` is the recorded demo of the working system.
- `Object_Center_Detection.png` shows the detected object center.
- `Frame_Center_Detection.png` shows the computed frame center.
- `marker_id.png` shows the markers generated and used in the demonstrations.

---

# Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/heyvarchas/proboticists-summer-training.git
   cd .\proboticists-summer-training\autonomous_subsystem\yolo-aruco-object-centering\
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install opencv-contrib-python ultralytics
   ```

4. Make sure your camera is connected and accessible from OpenCV.

---

# Usage

Run the main script:

```bash
python main.py
```

Notes:

- The current script uses `cv2.VideoCapture(2)`, so you may need to change the camera index if your system uses a different one.
- Press `Esc` to exit the window.

---

# How It Works

### YOLO Detection

The script loads the pretrained `yolov8n.pt` model and runs inference on every frame. It looks specifically for the `bottle` class. When a bottle is found, the code draws its bounding box and marks the object center using the midpoint of the bounding box.

### ArUco Detection

The program uses OpenCV’s ArUco module with the `DICT_4X4_50` dictionary. It detects all visible markers, calculates each marker’s center, and stores the centers in a dictionary using marker IDs as keys.

### Centering Logic

When markers `0, 1, 2, 3` are all present, the frame center is computed as the average of those four marker centers. The code then calculates:

- `dx = obj_x - frame_x`
- `dy = obj_y - frame_y`

A threshold of `15` pixels is used to decide whether the object is close enough to be considered centered. If the object is not centered, the script displays directions such as:

- `MOVE LEFT`
- `MOVE RIGHT`
- `MOVE UP`
- `MOVE DOWN`
- combined instructions like `MOVE LEFT UP`

If both offsets are within the threshold, the display shows `CENTERED`.

---

# Results

The system successfully:

- detects the target object in real time,
- detects all four ArUco markers,
- computes the frame center,
- computes the object center,
- draws a connecting line between the two centers,
- and displays movement guidance to help center the object.

The included screenshots and demo video show the detector working with a bottle placed inside the marker-based frame.

---

# Challenges Faced

- Detecting markers reliably when the camera angle was not ideal.
- Getting all four markers into the same frame at once.
- Camera index issues when switching between available cameras.
- Testing on a real floor setup where perspective and lighting affected detection.

These were handled by adjusting the camera setup, using DroidCam USB as an alternate input, and experimenting with the correct camera index until the feed worked correctly.

---

# Future Improvements

- Replace fixed movement instructions with PID-based control.
- Add serial communication to drive a robot or motor system directly.
- Support multiple target objects instead of only `bottle`.
- Add depth estimation for better centering in 3D space.
- Track objects and markers more robustly across frames.
- Make the target class and marker IDs configurable through a settings file.

---

# Dependencies

- `opencv-contrib-python`
- `ultralytics`

---

# Contributors

- Varchas Jasti

---

# License

MIT License.