# 🚨 AI Smart Surveillance System

A real-time AI-based surveillance system that detects, tracks, and triggers alerts when a human enters a defined security zone.

---

## 🎯 Features

* 🔍 Real-time human detection using YOLOv8
* 🎯 Object tracking with centroid-based tracking
* 🚨 ROI-based intrusion detection (security zone)
* ⚡ FPS monitoring (performance tracking)
* 💾 Video recording (output.avi)
* 📸 Automatic screenshot capture (intruder.jpg)

---

## 🧠 Technologies Used

* Python
* OpenCV
* YOLOv8 (Ultralytics)
* NumPy

---

## 🖥️ How It Works

1. The system captures video from a webcam
2. YOLOv8 detects humans in real-time
3. The tracker follows detected objects
4. If a person enters the defined ROI (security zone):

   * Alarm is triggered
   * Screenshot is saved
   * Event is recorded

---

## ▶️ Installation

```bash
git clone https://github.com/USERNAME/ai-smart-surveillance-system.git
cd ai-smart-surveillance-system
pip install -r requirements.txt
python main.py
```

---

## 📸 Demo

(Add your demo video or GIF here)

---

## 📂 Project Structure

```bash
main.py            # Main system
detector.py        # YOLO detection
tracker.py         # Object tracking
alarm.py           # Alarm system
```

---

## 🚀 Future Improvements

* Multi-object tracking with unique IDs
* Telegram alert system
* Cloud deployment
* Mobile notifications

---

## 👨‍💻 Author

Onur Günbek
