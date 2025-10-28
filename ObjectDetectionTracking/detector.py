from ultralytics import YOLO
import cv2
from deep_sort_realtime.deepsort_tracker import DeepSort

# Load YOLOv8 (n = fastest model)
model = YOLO("yolov8n.pt")

# Initialize Deep SORT
tracker = DeepSort(max_age=30, n_init=2, nms_max_overlap=1.0)

# Webcam (0) or replace with video path
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)[0]

    detections = []

    # YOLO detections → [x1, y1, x2, y2, confidence, class]
    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        conf = float(box.conf[0])
        cls = int(box.cls[0])

        if conf > 0.5:  # Ignore weak detections
            detections.append([x1, y1, x2 - x1, y2 - y1, conf, cls])

    # Send detections to Deep SORT
    tracks = tracker.update_tracks(detections, frame=frame)

    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        ltrb = track.to_ltrb()  # left, top, right, bottom
        x1, y1, x2, y2 = map(int, ltrb)

        label = model.names[track.get_det_class()]

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, f"{label} ID: {track_id}",
                    (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0,255,0), 2)

    cv2.imshow("YOLO + Deep SORT Object Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
