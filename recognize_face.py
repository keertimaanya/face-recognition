import face_recognition
import os
import numpy as np
import cv2

print("Starting camera...")

video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Camera not opening")
    exit()

print("Camera started")

dataset_path = "dataset"

known_encodings = []
known_names = []

# Load dataset
for person in os.listdir(dataset_path):

    person_folder = os.path.join(dataset_path, person)

    for image_name in os.listdir(person_folder):

        image_path = os.path.join(person_folder, image_name)

        try:
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)

            if len(encodings) > 0:
                known_encodings.append(encodings[0])
                known_names.append(person)

        except:
            print("Error loading image:", image_path)

print("Dataset loaded successfully")

while True:

    ret, frame = video.read()

    if not ret:
        print("Failed to grab frame")
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)

    for encoding, face in zip(encodings, faces):

        matches = face_recognition.compare_faces(known_encodings, encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_encodings, encoding)

        if len(face_distances) > 0:
            best_match = np.argmin(face_distances)

            if matches[best_match]:
                name = known_names[best_match]

        top, right, bottom, left = face

        cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
        cv2.putText(frame, name, (left, top-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()