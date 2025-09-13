import face_recognition as fr
import cv2
import os
import glob
import numpy as np

class Recognition:

    def __init__(self):

        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frame for a faster speed
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_folder):

        # Load Images
        images_path = glob.glob(os.path.join(images_folder, "*.*")) # Listing every file in the path containing dot in the filename.

        print("{} encoding images found.".format(len(images_path)))

        # Store image encoding and names
        for img_path in images_path:
            
            # Load image
            img = cv2.imread(img_path)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the filename only from the initial file path.
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)

            # Get encoding 
            img_encoding = fr.face_encodings(rgb_img)[0] # Returns a list of encodings from the faces in the image. Since it's only one face, index 0 is used.

            # Store file name and file encoding
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)

        print("Encoding images loaded.")

    def detect_known_faces(self, frame):

        # Resize frame for a faster speed
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)

        
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Find all the faces and face encodings in the current frame of video
        face_locations = fr.face_locations(rgb_small_frame)
        face_encodings = fr.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        
        for face_encoding in face_encodings:

            # See if the face is a match for the known face(s)
            matches = fr.compare_faces(self.known_face_encodings, face_encoding)

            # In case there is an unrecognized face
            name = "Unknown"

            # Use the known face with the smallest distance to the new face
            # Finding euclidean distance between the new face encoding and the recognized faces
            face_distances = fr.face_distance(self.known_face_encodings, face_encoding)

            # Index of the recognized face with the smallest distance to the new face
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                
                # Name of the best match
                name = self.known_face_names[best_match_index]

            # In case there are multiple faces in the frame
            face_names.append(name)

        # Convert to numpy array to adjust coordinates with frame resizing quickly
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing

        return face_locations.astype(int), face_names
