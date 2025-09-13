# **Real-Time Face Recognition with OpenCV and face_recognition**

This project demonstrates a real-time face recognition system using OpenCV and the `face_recognition` library. It detects and identifies faces from a webcam feed based on pre-encoded facial data.

## **📚 Introduction**

Face recognition technology allows computers to recognize and verify human faces from images or videos. This project captures video frames using your webcam, detects faces in real-time, and identifies them based on prior training images stored in a local directory.

<br>

## **🏗️ Project Architecture**

- load_cam.py # Main script to start webcam and display recognition results
- recognition.py # Face encoding and recognition logic
- requirements.txt # Required Python packages
- images/ # Folder containing images for training (1 face per image):
  - Danial.jpg
  - Parsa.jpg
  - Elon Musk.jpg
  - and other pictures...

<br>

### **🔄 Module Flow**

1. **`recognition.py`**: Loads and encodes faces from the `images/` folder.
2. **`load_cam.py`**:
   - Captures frames from the webcam.
   - Uses `Recognition` class to detect and identify faces.
   - Displays names and bounding boxes in real-time.

<br>  

Visit [Face Recognition Project/Code_Documentation.md](Code_Documentation.md) for complete documentation on the classes and functions used.

<br>

## **Installation and Setup**
- In order for the project to run successfully, you need to first install [CMake](https://cmake.org/download/) (Click on the link to download and install your preferred version of CMake).

- Ensure you have Python 3.6+ installed. Then install all required packages using:

    ```shell
    pip install -r requirements.txt
    ```

### **Prepare training images**

Add your reference images to the `images/` directory. Each image:

- Should contain only one face.

- Should be named uniquely (e.g., Parsa.jpg, Danial.jpg).

- The filename (without extension) will be used as the label for recognition.


### **🚀 Usage**

**Run the application with:**
```shell
python load_cam.py
```
A window will open showing your webcam feed.

Detected faces will be labeled based on the `images/` encodings.

Press `Esc` to quit the application.

<br>

## **📦 Dependencies**
Project dependencies are listed in `requirements.txt` file, **including**:

- **[face_recognition](https://github.com/ageitgey/face_recognition)**

- **[opencv-python](https://pypi.org/project/opencv-python/)**

- **[numpy](https://numpy.org/)**

<br>

----
### Developed by Danial Goodarzi & Parsa Nasiri

### Supervised by Professor Mohammad Misagh Javaherian

### at Shamsipour National University of Skills
----
