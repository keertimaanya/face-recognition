# Face Recognition System using OpenCV

A real-time face recognition system built using **Python, OpenCV, and the face_recognition library**.
The system detects faces from a webcam feed and recognizes known individuals from a dataset.

---

## Features

* Real-time face detection using webcam
* Face recognition using preloaded dataset
* Draws bounding boxes around detected faces
* Displays the name of the recognized person
* Handles unknown faces

---

## Technologies Used

* Python
* OpenCV
* face_recognition (dlib based)
* NumPy

---

## Project Structure

```
face-recognition-opencv
│
├── dataset
│   ├── Person1
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   │
│   ├── Person2
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│
├── recognize_face.py
├── requirements.txt
├── .gitignore
└── README.md
```

Each folder inside **dataset** represents a person.
Images inside the folder are used to train the face recognition system.

---

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/face-recognition-opencv.git
```

Navigate to the project folder:

```
cd face-recognition-opencv
```

Install required libraries:

```
pip install -r requirements.txt
```

---

## Run the Project

Run the face recognition script:

```
python recognize_face.py
```

The webcam will open and the system will start detecting and recognizing faces.

Press **Q** to exit the camera.

---

## Example Use Case

This project can be used for:

* Basic face recognition systems
* Attendance systems
* Security systems
* Learning computer vision concepts

---

## Future Improvements

* Add face registration feature
* Improve recognition accuracy
* Deploy as a web application
* Add GUI interface

---

## Author

Keerti Maanya
