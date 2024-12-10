from face_recognition import load_known_faces, recognize_faces
from database import init_db, mark_attendance, fetch_attendance
from utils import debounce

@debounce
def process_recognition(name):
    if name != "Unknown":
        mark_attendance(name)

def main():
    init_db()
    known_encodings, known_names = load_known_faces()

    for recognized_name in recognize_faces(known_encodings, known_names):
        process_recognition(recognized_name)

if __name__ == "__main__":
    main()
