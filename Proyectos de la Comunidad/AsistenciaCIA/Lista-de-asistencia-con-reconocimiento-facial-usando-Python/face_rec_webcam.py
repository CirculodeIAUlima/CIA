import face_recognition
import cv2
import numpy as np

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
Alexander_Daniel_Roman_Gabriel_image = face_recognition.load_image_file("Alexander_Daniel_Roman_Gabriel.jpg")
Alexander_Daniel_Roman_Gabriel_face_encoding = face_recognition.face_encodings(Alexander_Daniel_Roman_Gabriel_image)[0]
# Load a sample picture and learn how to recognize it.
Jesus_Sebastian_Diez_Plasencia_image = face_recognition.load_image_file("Jesus_Sebastian_Diez_Plasencia.jpg")
Jesus_Sebastian_Diez_Plasencia_face_encoding = face_recognition.face_encodings(Jesus_Sebastian_Diez_Plasencia_image)[0]
# Load a sample picture and learn how to recognize it.
Gabriel_Lozano_Chavez_image = face_recognition.load_image_file("Gabriel_Lozano_Chavez.jpg")
Gabriel_Lozano_Chavez_face_encoding = face_recognition.face_encodings(Gabriel_Lozano_Chavez_image)[0]
# Load a sample picture and learn how to recognize it.
Ners_Armando_Vasquez_Espinoza_image = face_recognition.load_image_file("Ners_Armando_Vasquez_Espinoza.jpg")
Ners_Armando_Vasquez_Espinoza_face_encoding = face_recognition.face_encodings(Ners_Armando_Vasquez_Espinoza_image)[0]
# Load a sample picture and learn how to recognize it.
Ignacio_de_Jesús_Medina_Urrunaga_image = face_recognition.load_image_file("Ignacio_de_Jesús_Medina_Urrunaga.jpg")
Ignacio_de_Jesús_Medina_Urrunaga_face_encoding = face_recognition.face_encodings(Ignacio_de_Jesús_Medina_Urrunaga_image)[0]
# Load a sample picture and learn how to recognize it.
Renato_Marcelo_Migliori_Ruiz_image = face_recognition.load_image_file("Renato_Marcelo_Migliori_Ruiz.jpg")
Renato_Marcelo_Migliori_Ruiz_face_encoding = face_recognition.face_encodings(Renato_Marcelo_Migliori_Ruiz_image)[0]
# Load a sample picture and learn how to recognize it.
Adrian_Alexander_Flores_Uzategui_image = face_recognition.load_image_file("Adrian_Alexander_Flores_Uzategui.jpg")
Adrian_Alexander_Flores_Uzategui_face_encoding = face_recognition.face_encodings(Adrian_Alexander_Flores_Uzategui_image)[0]
# Load a sample picture and learn how to recognize it.
Andrea_Pilar_Llerena_Zuñiga_image = face_recognition.load_image_file("Andrea_Pilar_Llerena_Zuñiga.jpg")
Andrea_Pilar_Llerena_Zuñiga_face_encoding = face_recognition.face_encodings(Andrea_Pilar_Llerena_Zuñiga_image)[0]
# Load a sample picture and learn how to recognize it.
Renzo_Fabrizzio_Saucedo_Soria_image = face_recognition.load_image_file("Renzo_Fabrizzio_Saucedo_Soria.jpg")
Renzo_Fabrizzio_Saucedo_Soria_face_encoding = face_recognition.face_encodings(Renzo_Fabrizzio_Saucedo_Soria_image)[0]
# Load a sample picture and learn how to recognize it.
Valeria_Alexandra_Almanza_Lopez_image = face_recognition.load_image_file("Valeria_Alexandra_Almanza_Lopez.jpg")
Valeria_Alexandra_Almanza_Lopez_face_encoding = face_recognition.face_encodings(Valeria_Alexandra_Almanza_Lopez_image)[0]
# Load a sample picture and learn how to recognize it.
Manuel_Nazaret_Zambrano_Moran_image = face_recognition.load_image_file("Manuel_Nazaret_Zambrano_Moran.jpg")
Manuel_Nazaret_Zambrano_Moran_face_encoding = face_recognition.face_encodings(Manuel_Nazaret_Zambrano_Moran_image)[0]
# Load a sample picture and learn how to recognize it.
Gary_Gabriel_Sandoval_Ramos_image = face_recognition.load_image_file("Gary_Gabriel_Sandoval_Ramos.jpg")
Gary_Gabriel_Sandoval_Ramos_face_encoding = face_recognition.face_encodings(Gary_Gabriel_Sandoval_Ramos_image)[0]
# Load a sample picture and learn how to recognize it.
Gabriel_Andres_Tineo_Morales_image = face_recognition.load_image_file("Gabriel_Andres_Tineo_Morales.jpg")
Gabriel_Andres_Tineo_Morales_face_encoding = face_recognition.face_encodings(Gabriel_Andres_Tineo_Morales_image)[0]
# Load a sample picture and learn how to recognize it.
Angello_Alejandro_Cusque_Oropeza_image = face_recognition.load_image_file("Angello_Alejandro_Cusque_Oropeza.jpg")
Angello_Alejandro_Cusque_Oropeza_face_encoding = face_recognition.face_encodings(Angello_Alejandro_Cusque_Oropeza_image)[0]
# Load a sample picture and learn how to recognize it.
Sofia_Pinaya_Vargas_image = face_recognition.load_image_file("Sofia_Pinaya_Vargas.jpg")
Sofia_Pinaya_Vargas_face_encoding = face_recognition.face_encodings(Sofia_Pinaya_Vargas_image)[0]
# Load a sample picture and learn how to recognize it.
Jeremin_Junior_Roman_Gabriel_image = face_recognition.load_image_file("Jeremin_Junior_Roman_Gabriel.jpg")
Jeremin_Junior_Roman_Gabriel_face_encoding = face_recognition.face_encodings(Jeremin_Junior_Roman_Gabriel_image)[0]
# Load a sample picture and learn how to recognize it.
Alessandra_Nicole_Uribe_Encina_image = face_recognition.load_image_file("Alessandra_Nicole_Uribe_Encina.jpg")
Alessandra_Nicole_Uribe_Encina_face_encoding = face_recognition.face_encodings(Alessandra_Nicole_Uribe_Encina_image)[0]
# Load a sample picture and learn how to recognize it.
Claudia_Patricia_Sipion_Guillen_image = face_recognition.load_image_file("Claudia_Patricia_Sipion_Guillen.jpg")
Claudia_Patricia_Sipion_Guillen_face_encoding = face_recognition.face_encodings(Claudia_Patricia_Sipion_Guillen_image)[0]


# Create arrays of known face encodings and their names
known_face_encodings = [
    Alexander_Daniel_Roman_Gabriel_face_encoding,
    Jesus_Sebastian_Diez_Plasencia_face_encoding,
    Gabriel_Lozano_Chavez_face_encoding,
    Ners_Armando_Vasquez_Espinoza_face_encoding,
    Ignacio_de_Jesús_Medina_Urrunaga_face_encoding,
    Renato_Marcelo_Migliori_Ruiz_face_encoding,
    Adrian_Alexander_Flores_Uzategui_face_encoding,
    Andrea_Pilar_Llerena_Zuñiga_face_encoding,
    Renzo_Fabrizzio_Saucedo_Soria_face_encoding,
    Valeria_Alexandra_Almanza_Lopez_face_encoding,
    Manuel_Nazaret_Zambrano_Moran_face_encoding,
    Gary_Gabriel_Sandoval_Ramos_face_encoding,
    Gabriel_Andres_Tineo_Morales_face_encoding,
    Angello_Alejandro_Cusque_Oropeza_face_encoding,
    Sofia_Pinaya_Vargas_face_encoding,
    Jeremin_Junior_Roman_Gabriel_face_encoding,
    Alessandra_Nicole_Uribe_Encina_face_encoding,
    Claudia_Patricia_Sipion_Guillen_face_encoding
]
known_face_names = [
    "Alexander_Daniel_Roman_Gabriel",
    "Jesus_Sebastian_Diez_Plasencia",
    "Gabriel_Lozano_Chavez",
    "Ners_Armando_Vasquez_Espinoza",
    "Ignacio_de_Jesús_Medina_Urrunaga",
    "Renato_Marcelo_Migliori_Ruiz",
    "Adrian_Alexander_Flores_Uzategui",
    "Andrea_Pilar_Llerena_Zuñiga",
    "Renzo_Fabrizzio_Saucedo_Soria",
    "Valeria_Alexandra_Almanza_Lopez",
    "Manuel_Nazaret_Zambrano_Moran",
    "Gary_Gabriel_Sandoval_Ramos",
    "Gabriel_Andres_Tineo_Morales",
    "Angello_Alejandro_Cusque_Oropeza",
    "Sofia_Pinaya_Vargas",
    "Jeremin_Junior_Roman_Gabriel",
    "Alessandra_Nicole_Uribe_Encina",
    "Claudia_Patricia_Sipion_Guillen"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        #rgb_small_frame = small_frame[:, :, ::-1]
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
