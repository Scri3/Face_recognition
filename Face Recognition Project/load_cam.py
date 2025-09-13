import cv2
from recognition import Recognition

# Encode faces from a folder
face_rec = Recognition()
face_rec.load_encoding_images(r"images/")

# Load Camera
cam = cv2.VideoCapture(0)


while True:

    # Getting frames
    ret, frame = cam.read()

    # Detect Faces
    face_locations, face_names = face_rec.detect_known_faces(frame)

    # cv2 operations
    for face_loc, name in zip(face_locations, face_names):

        # Naming coordinates
        top, right, bottom, left = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        # Showing the person's name and drawing rectangle around the face
        cv2.putText(frame, name,(left, top - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 255), 4)

    # Show the frame (realtime)
    cv2.imshow("Webcam", frame)

    # Exit the loop 1ms after "Escape" button is pressed
    key = cv2.waitKey(1)

    if key == 27:
        
        break

cam.release()
cv2.destroyAllWindows()