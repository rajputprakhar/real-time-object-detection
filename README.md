# Real-Time Object Detection using YOLOv8 

A real-time computer vision application that detects and classifies objects via webcam using the YOLOv8 (You Only Look Once) model. Built with Python and OpenCV.

##  Features
- **Real-Time Detection:** Processes video feed instantly from the webcam.
- **High Accuracy:** Uses the pre-trained YOLOv8 Nano model for efficient detection.
- **Visual Feedback:** Draws bounding boxes and labels around detected objects (e.g., Person, Cell Phone, Cup).

##  Tech Stack
- **Language:** Python 3.x
- **Computer Vision:** OpenCV (`cv2`)
- **AI Model:** Ultralytics YOLOv8
- **Environment:** VS Code

##  Installation & Setup

1. **Clone the repository**
```
   git clone [https://github.com/YOUR_USERNAME/real-time-object-detection.git](https://github.com/rajputprakhar/real-time-object-detection.git)
   cd real-time-object-detection
```

## Create a Virtual Environment (Recommended)

```
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

```
##Install Dependencies

```
pip install -r requirements.txt

```
##▶️ How to Run

Run the main script to start the webcam feed:

```
python main.py

```
Press 'q' to quit the application.

Created by Prakhar Rajput
