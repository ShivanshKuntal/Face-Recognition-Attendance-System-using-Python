---

# Face Recognition Attendance System

This project implements an automated attendance system using real-time face recognition. It detects faces from a webcam feed, identifies registered students using a trained classifier, and logs attendance into a CSV file.

---



<img width="1279" height="715" alt="image" src="https://github.com/user-attachments/assets/14c2046c-68f0-41ac-9612-81e6a8ebe70a" />


------


## 📂 Project Files Overview

* **main.py** – Runs the face recognition attendance system
* **train.py** – Trains the classifier using student images
* **student.py** – Handles student data entry and image capture
* **face_recognition.py** – Core recognition logic (LBPH / OpenCV-based)
* **attendance.py** – Updates and stores attendance in `attendance.csv`
* **help.py** – Utility/helper functions
* **haarcascade_frontalface_default.xml** – Haarcascade model for face detection
* **classifier.zip** – Trained LBPH model
* **attendance.csv** – Auto-generated attendance records

---

## 🚀 How It Works

1. **Face Detection:**
   Haarcascade model identifies faces from webcam input.

2. **Face Recognition:**
   LBPH classifier compares detected faces with trained dataset.

3. **Attendance Logging:**
   Recognized student name, ID, timestamp are saved in `attendance.csv`.

4. **Model Training:**
   Run `train.py` after adding new student images to update the classifier.

---

## ▶️ Running the System

```bash
python main.py
```

To train the model:

```bash
python train.py
```

---

## 🛠️ Requirements

* Python
* OpenCV
* Numpy
* Pandas

---

## ⚠️ Note

This system is built for academic demonstration.
Accuracy depends on lighting conditions, training image quality, and camera resolution.

