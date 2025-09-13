# 📄 Code Documentation for Real-Time Face Recognition

This document provides detailed descriptions of the classes and functions used in the files `recognition.py` and `load_cam.py`.

---

## 📄 recognition.py

### Class: `Recognition`
Encapsulates face encoding and recognition logic using the `face_recognition` library.

#### `__init__(self)`
Initializes the recognition system.

- `self.known_face_encodings`: Stores facial encoding vectors of known individuals.
- `self.known_face_names`: Stores names corresponding to the known face encodings.
- `self.frame_resizing`: Factor used to downscale frames for faster processing.

---

#### `load_encoding_images(self, images_folder)`
Encodes all images in the specified folder and stores their encodings and names.

- **Parameters:**
  - `images_folder` (str): Path to the folder containing face images (one face per image).
- **Process:**
  - Reads all images from the folder.
  - Converts each image from BGR to RGB.
  - Extracts the face encoding and stores it along with the image name (filename without extension).
- **Usage:** Must be called before attempting face recognition.
- **Prints:** Number of images found and a success message.

---

#### `detect_known_faces(self, frame)`
Detects and recognizes faces in a video frame.

- **Parameters:**
  - `frame` (numpy.ndarray): The current video frame in BGR format.
- **Returns:**
  - `face_locations` (np.ndarray): List of bounding box coordinates for detected faces.
  - `face_names` (List[str]): Names of recognized individuals or `'Unknown'`.
- **Process:**
  - Resizes the frame to speed up recognition.
  - Converts the frame to RGB format.
  - Detects all face locations and encodings.
  - Compares with known face encodings using Euclidean distance and a similarity threshold.

---

## 📄 load_cam.py

Main script for running real-time face recognition through the webcam.

#### Global Execution

```python
face_rec = Recognition()
face_rec.load_encoding_images(r"images/")
cam = cv2.VideoCapture(0)
```

- **Initializes** the `Recognition` class and loads known face encodings from the `images/` directory.
- **Starts** the webcam using OpenCV.

---

#### `while True:` loop

- Continuously reads frames from the webcam.
- Calls `detect_known_faces(frame)` from `Recognition`.
- Draws rectangles and labels around detected faces in the video stream.
- Displays the modified frame in a GUI window.
- Breaks the loop and closes the webcam if the **Escape (ESC)** key is pressed.

---

#### Functions used (OpenCV)

- `cv2.VideoCapture(0)`: Opens webcam.
- `cv2.putText(...)`: Adds text labels to video frames.
- `cv2.rectangle(...)`: Draws bounding boxes.
- `cv2.imshow(...)`: Shows the processed video in real time.
- `cv2.waitKey(1)`: Checks for key presses.