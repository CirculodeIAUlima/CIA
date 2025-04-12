import face_recognition
import cv2
import numpy as np
import mysql.connector
from datetime import datetime
import os

# Establishes connection with the MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="root",
    database="attendance_db"
)
db_cursor = db_connection.cursor()

# Creates the 'registration' table if it does not exist in the database
create_table_query = """
CREATE TABLE IF NOT EXISTS registration (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    name VARCHAR(100) NOT NULL,
    time TIME NOT NULL
);
"""
db_cursor.execute(create_table_query)

# Lists to store encodings and names of known faces
known_face_encodings = []
known_face_names = []
# Path to the folder with images of known people
destiny_path = "Images"

# Iterates over images in the specified folder and generates encodings
for filename in os.listdir(destiny_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = face_recognition.load_image_file(os.path.join(destiny_path, filename))
        face_encoding = face_recognition.face_encodings(image)
        if face_encoding:
            known_face_encodings.append(face_encoding[0])
            known_face_names.append(filename.split(".")[0])
        else:
            print(f"Could not find a face in {filename}")

# Initializes variables for facial recognition
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# Accesses the device's webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Captures the current image from the webcam
    ret, frame = video_capture.read()

    # Processes only some frames to optimize speed
    if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Identifies faces in the image
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Compares the detected face with known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            # If the face is not recognized (not in destiny_path), the default label is "Unknown"
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

                # Gets the current date and time
                now = datetime.now()
                current_date = now.date()
                current_time = now.time()

                # Checks if the person has already been registered for the day
                check_query = "SELECT * FROM registration WHERE name = %s AND date = %s"
                db_cursor.execute(check_query, (name, current_date))
                result = db_cursor.fetchone()

                if not result:
                    # If not registered, adds a new record to the database
                    insert_query = "INSERT INTO registration (date, name, time) VALUES (%s, %s, %s)"
                    db_cursor.execute(insert_query, (current_date, name, current_time))
                    db_connection.commit()
                else:
                    print(f"{name} has already been registered today")

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Displays the result in the window
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    # Ends the program if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Releases the webcam and closes the windows
video_capture.release()
cv2.destroyAllWindows()
