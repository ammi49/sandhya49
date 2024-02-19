import cv2
import os

# Load the image
image_path = "C:\\Users\\Admin\\Pictures\\Camera Roll\\WIN_20240202_15_10_27_Pro.jpg"
image = cv2.imread(image_path)

# Check if image is loaded successfully
if image is None:
    print("Error: Unable to load image.")
    exit()

# Perform face detection (you may have already done this using a face detection algorithm)
# For example, using OpenCV's pre-trained Haarcascades classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(image, scaleFactor=1.3, minNeighbors=5)

# Create a folder to save the images with faces
output_folder = r"D:\salian"
os.makedirs(output_folder, exist_ok=True)

# Save images with faces
for i, (x, y, w, h) in enumerate(faces):
    face_image = image[y:y+h, x:x+w]
    save_path = os.path.join(output_folder, f"face_{i+1}.jpg")
    cv2.imwrite(save_path, face_image)
    print(f"Face {i+1} saved at: {save_path}")
