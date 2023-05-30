import streamlit as st
import cv2
import face_recognition
import time
# Define a function to detect the skin tone of a face
def detect_skin_tone(image):
    
    # Detect the face locations
    face_locations = face_recognition.face_locations(image)
    # If no face is detected, return None
    if not face_locations:
        return None
    # Extract the face from the image
    top, right, bottom, left = face_locations[0]
    face_image = image[top:bottom, left:right]
    # Compute the skin tone of the face
    mean_color = face_image.mean(axis=(0, 1))
    # Determine the skin tone based on the mean color
    if mean_color[0] > 95 and mean_color[1] > 40 and mean_color[2] > 20:
        return "Fair"
    elif mean_color[0] > 65 and mean_color[1] > 25 and mean_color[2] > 10:
        return "Dusky"
    else:
        return "Brown"

# Create a Streamlit app
def main():
    # Set app title
    st.title("Skin Tone Detector")

    # Open a camera input
    cap = cv2.VideoCapture(0)

    # Start the main loop
    while True:
        time.sleep(1)
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to read frame from camera")
            break
        
        

        # Convert the image to RGB format
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect the skin tone of the face in the frame
        skin_tone = detect_skin_tone(rgb_frame)

        # Display the result on the app
        if skin_tone:
            
            cv2.putText(frame, skin_tone, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            st.image(frame, channels="BGR")
            st.success(f"Skin detected: {skin_tone}")
            st.stop()

    cap.release()

if __name__ == "__main__":
    main()
