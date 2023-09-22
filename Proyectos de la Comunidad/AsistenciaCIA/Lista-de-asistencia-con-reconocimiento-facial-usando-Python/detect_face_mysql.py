import face_recognition
import cv2
import numpy as np
import mysql.connector
from datetime import datetime

# pip install face_recognition
# pip install opencv-python

# Conexion a la base de datos de mysql
db_connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="root",
    database="asistencia_del_cia"
)
db_cursor = db_connection.cursor()

# crear la tabla registro si no existe;
create_table_query = """
CREATE TABLE IF NOT EXISTS registro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    hora TIME NOT NULL
);
"""

db_cursor.execute(create_table_query)

# cargar imagen a reconocer
Alexander_Daniel_Roman_Gabriel_image = face_recognition.load_image_file("Alexander_Daniel_Roman_Gabriel.jpg")
Alexander_Daniel_Roman_Gabriel_face_encoding = face_recognition.face_encodings(Alexander_Daniel_Roman_Gabriel_image)[0]
# cargar imagen a reconocer
Jesus_Sebastian_Diez_Plasencia_image = face_recognition.load_image_file("Jesus_Sebastian_Diez_Plasencia.jpg")
Jesus_Sebastian_Diez_Plasencia_face_encoding = face_recognition.face_encodings(Jesus_Sebastian_Diez_Plasencia_image)[0]
# cargar imagen a reconocer
Gabriel_Lozano_Chavez_image = face_recognition.load_image_file("Gabriel_Lozano_Chavez.jpg")
Gabriel_Lozano_Chavez_face_encoding = face_recognition.face_encodings(Gabriel_Lozano_Chavez_image)[0]
# cargar imagen a reconocer
Ners_Armando_Vasquez_Espinoza_image = face_recognition.load_image_file("Ners_Armando_Vasquez_Espinoza.jpg")
Ners_Armando_Vasquez_Espinoza_face_encoding = face_recognition.face_encodings(Ners_Armando_Vasquez_Espinoza_image)[0]
# cargar imagen a reconocer
Ignacio_de_Jesús_Medina_Urrunaga_image = face_recognition.load_image_file("Ignacio_de_Jesús_Medina_Urrunaga.jpg")
Ignacio_de_Jesús_Medina_Urrunaga_face_encoding = face_recognition.face_encodings(Ignacio_de_Jesús_Medina_Urrunaga_image)[0]
# cargar imagen a reconocer
Renato_Marcelo_Migliori_Ruiz_image = face_recognition.load_image_file("Renato_Marcelo_Migliori_Ruiz.jpg")
Renato_Marcelo_Migliori_Ruiz_face_encoding = face_recognition.face_encodings(Renato_Marcelo_Migliori_Ruiz_image)[0]
# cargar imagen a reconocer
Adrian_Alexander_Flores_Uzategui_image = face_recognition.load_image_file("Adrian_Alexander_Flores_Uzategui.jpg")
Adrian_Alexander_Flores_Uzategui_face_encoding = face_recognition.face_encodings(Adrian_Alexander_Flores_Uzategui_image)[0]
# cargar imagen a reconocer
Andrea_Pilar_Llerena_Zuñiga_image = face_recognition.load_image_file("Andrea_Pilar_Llerena_Zuñiga.jpg")
Andrea_Pilar_Llerena_Zuñiga_face_encoding = face_recognition.face_encodings(Andrea_Pilar_Llerena_Zuñiga_image)[0]
# cargar imagen a reconocer
Renzo_Fabrizzio_Saucedo_Soria_image = face_recognition.load_image_file("Renzo_Fabrizzio_Saucedo_Soria.jpg")
Renzo_Fabrizzio_Saucedo_Soria_face_encoding = face_recognition.face_encodings(Renzo_Fabrizzio_Saucedo_Soria_image)[0]
# cargar imagen a reconocer
Valeria_Alexandra_Almanza_Lopez_image = face_recognition.load_image_file("Valeria_Alexandra_Almanza_Lopez.jpg")
Valeria_Alexandra_Almanza_Lopez_face_encoding = face_recognition.face_encodings(Valeria_Alexandra_Almanza_Lopez_image)[0]
# cargar imagen a reconocer
Manuel_Nazaret_Zambrano_Moran_image = face_recognition.load_image_file("Manuel_Nazaret_Zambrano_Moran.jpg")
Manuel_Nazaret_Zambrano_Moran_face_encoding = face_recognition.face_encodings(Manuel_Nazaret_Zambrano_Moran_image)[0]
# cargar imagen a reconocer
Gary_Gabriel_Sandoval_Ramos_image = face_recognition.load_image_file("Gary_Gabriel_Sandoval_Ramos.jpg")
Gary_Gabriel_Sandoval_Ramos_face_encoding = face_recognition.face_encodings(Gary_Gabriel_Sandoval_Ramos_image)[0]
# cargar imagen a reconocer
Gabriel_Andres_Tineo_Morales_image = face_recognition.load_image_file("Gabriel_Andres_Tineo_Morales.jpg")
Gabriel_Andres_Tineo_Morales_face_encoding = face_recognition.face_encodings(Gabriel_Andres_Tineo_Morales_image)[0]
# cargar imagen a reconocer
Angello_Alejandro_Cusque_Oropeza_image = face_recognition.load_image_file("Angello_Alejandro_Cusque_Oropeza.jpg")
Angello_Alejandro_Cusque_Oropeza_face_encoding = face_recognition.face_encodings(Angello_Alejandro_Cusque_Oropeza_image)[0]
# cargar imagen a reconocer
Sofia_Pinaya_Vargas_image = face_recognition.load_image_file("Sofia_Pinaya_Vargas.jpg")
Sofia_Pinaya_Vargas_face_encoding = face_recognition.face_encodings(Sofia_Pinaya_Vargas_image)[0]
# cargar imagen a reconocer
Jeremin_Junior_Roman_Gabriel_image = face_recognition.load_image_file("Jeremin_Junior_Roman_Gabriel.jpg")
Jeremin_Junior_Roman_Gabriel_face_encoding = face_recognition.face_encodings(Jeremin_Junior_Roman_Gabriel_image)[0]
# cargar imagen a reconocer
Alessandra_Nicole_Uribe_Encina_image = face_recognition.load_image_file("Alessandra_Nicole_Uribe_Encina.jpg")
Alessandra_Nicole_Uribe_Encina_face_encoding = face_recognition.face_encodings(Alessandra_Nicole_Uribe_Encina_image)[0]
# cargar imagen a reconocer
Claudia_Patricia_Sipion_Guillen_image = face_recognition.load_image_file("Claudia_Patricia_Sipion_Guillen.jpg")
Claudia_Patricia_Sipion_Guillen_face_encoding = face_recognition.face_encodings(Claudia_Patricia_Sipion_Guillen_image)[0]


# Create arrays of known face encodings and their names
# Crear arreglos de los encodings de caras conocidas
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

# Iniciar variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# Instancia de la webcam a usar
video_capture = cv2.VideoCapture(0)

while True:
    # Capturar frames
    ret, frame = video_capture.read()


    # procesa una parte de la imagen para hacer más rapido el codigo
    if process_this_frame:
        
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        #  Convertir a RGB ya que opencv lee BGR
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Encuentra todos los rostros
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Busca matchs en los rostros conocidos
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # o busca un match al mas cercano
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

                # fecha y hora actual
                now = datetime.now()
                current_date = now.date()
                current_time = now.time()

                # checa si no ha sido registrado el día de hoy
                check_query = "SELECT * FROM registro WHERE nombre = %s AND fecha = %s"
                db_cursor.execute(check_query, (name, current_date))
                result = db_cursor.fetchone()

                if not result:
                    # Inserta el registro en la base  de datos
                    insert_query = "INSERT INTO registro (fecha, nombre, hora) VALUES (%s, %s, %s)"
                    db_cursor.execute(insert_query, (current_date, name, current_time))
                    db_connection.commit()
                else:
                    print(f"{name} Ya ha sido registrado el dia de hoy")

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Muestra los resultados
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Reescala la imagen con el rostro
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Dibuja el rectangulo con el rostro
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Dibuja etiqueta con el nombre
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Muestra la imagen con el resultado de la detección
    cv2.imshow('Video', frame)

    # Oprimir tecla q para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cierra la webcam
video_capture.release()
cv2.destroyAllWindows()
