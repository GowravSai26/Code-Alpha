# Code Alpha 🚀 AI Projects Repository

This repository contains two practical AI/ML projects demonstrating both **NLP (Natural Language Processing)** and **Computer Vision** concepts.

---

## 📂 Projects Included

### 1) 🤖 FAQ Chatbot (NLP + Streamlit)

A simple chatbot that answers frequently asked questions by matching the user's query with the most similar FAQ using **TF-IDF** and **Cosine Similarity**.

#### ✅ Features
- Stores FAQs in a separate JSON file
- Text preprocessing + vector similarity matching
- Clean Streamlit UI for interaction
- Easy to expand by simply adding more FAQs

#### 📌 Tech Used
| Component | Tool |
|----------|------|
| Vectorization | TF-IDF (Scikit-Learn) |
| Similarity Matching | Cosine Similarity |
| UI | Streamlit |
| Data Storage | JSON |

#### ▶️ Run
```bash
cd ChatbotForFAQs
streamlit run app.py
````

---

### 2) 🎯 Object Detection & Tracking (YOLO + Deep SORT)

Real-time multi-object detection and identity-aware tracking using webcam input.
Objects keep the **same tracking ID** even when moving or re-entering the frame.

#### ✅ Features

* YOLOv8 for object detection
* Deep SORT for stable tracking
* Works on webcam or video input
* Displays bounding boxes, class names, and unique IDs

#### 📌 Tech Used

| Component        | Tool                 |
| ---------------- | -------------------- |
| Object Detection | YOLOv8 (Ultralytics) |
| Object Tracking  | Deep SORT            |
| Video Processing | OpenCV               |

#### ▶️ Run

```bash
cd ObjectDetectionTracking
python detector.py
```

---

## 🧠 Learning Outcomes

| Skill                      | Demonstrated In | Description                                     |
| -------------------------- | --------------- | ----------------------------------------------- |
| NLP Text Processing        | Chatbot         | Tokenization, vectorization, similarity scoring |
| ML Model Usage             | Both            | Using pre-trained models effectively            |
| Real-Time Video Processing | Object Tracking | Handling continuous frame streams               |
| Computer Vision            | Object Tracking | Detection + bounding box drawing                |
| UI Development             | Chatbot         | Streamlit-based interactive interface           |

---

## 📁 Repository Structure

```
AI-Mini-Projects/
│
├── ChatbotForFAQs/              # Project 1
│   ├── app.py
│   ├── chatbot.py
│   ├── faqs.json
│   └── requirements.txt
│
└── ObjectDetectionTracking/     # Project 2
    ├── detector.py
    ├── sort.py  (if using SORT)
    ├── requirements.txt
```



## 📝 Setup Instructions (Root)

Install project dependencies :

```bash
pip install -r requirements.txt
```
---

## 👤 Author

GOWRAV SAI VEERAMALLU
