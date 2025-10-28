# 🎯 Object Detection and Tracking using YOLO + Deep SORT

This project performs **real-time object detection and identity-aware tracking** using a webcam or video input.  
It combines **YOLOv8** for object detection and **Deep SORT** for tracking, which ensures that the **same object keeps the same ID** even when it moves, overlaps, or leaves/re-enters the frame.

---

## ✅ Features
- Real-time video input (webcam / video file)
- Fast and accurate object detection with **YOLOv8**
- Stable object tracking using **Deep SORT (ReID model)**
- Each object gets a **unique and consistent tracking ID**
- Displays bounding boxes, object class labels, and tracking IDs

---

## 🗂️ Project Structure
```

ObjectDetectionTracking/
│
├─ detector.py          # YOLO + Deep SORT main program
└─ requirements.txt     # Dependencies

````

---

## 📦 Requirements

### Install dependencies
```bash
pip install -r requirements.txt
````

### Or install manually:

```bash
pip install ultralytics opencv-python numpy deep-sort-realtime
```

> *Deep SORT uses a ReID (appearance feature) model internally — no extra setup needed.*

---

## ▶️ How to Run

### 1) Run with Webcam

```bash
python detector.py
```

### 2) Run on a Video File (optional)

In `detector.py`, replace:

```python
cap = cv2.VideoCapture(0)
```

with:

```python
cap = cv2.VideoCapture("your_video.mp4")
```

---

## 🤖 How It Works

| Step | Description                                                                           |
| ---- | ------------------------------------------------------------------------------------- |
| 1    | YOLOv8 detects objects in each frame                                                  |
| 2    | Bounding boxes, class labels, and confidence scores are extracted                     |
| 3    | These detections are passed to **Deep SORT**                                          |
| 4    | Deep SORT assigns and maintains **unique track IDs** using motion + appearance (ReID) |
| 5    | Output video is displayed with boxes and IDs                                          |

---

## 🧠 Why Deep SORT?

Unlike regular SORT, **Deep SORT tracks identity, not just motion**.

| Feature                          | SORT | **Deep SORT (used here)** |
| -------------------------------- | ---- | ------------------------- |
| Tracks based on position only    | ✅    | ❌                         |
| Uses visual appearance (ReID)    | ❌    | ✅                         |
| Keeps same ID after occlusion    | ❌    | ✅                         |
| Handles multiple similar objects | ❌    | ✅                         |

Deep SORT = **Stable, real-world tracking** ✅

---

## 🎯 Example Output

```
person ID: 3
cup ID: 1
bottle ID: 0
```

IDs **stay consistent** even when objects move around.

---

## ✅ Task Requirements (Completed)

| Requirement                                  | Status |
| -------------------------------------------- | ------ |
| Real-time video input                        | ✅      |
| Use pre-trained YOLO model                   | ✅      |
| Detect objects and draw bounding boxes       | ✅      |
| Apply object tracking (Deep SORT)            | ✅      |
| Display labels and tracking IDs in real-time | ✅      |


---