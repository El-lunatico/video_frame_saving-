import os
import cv2
import numpy as np
from flask import Flask, render_template, request
import time

app = Flask(__name__)

# Directory to save frames
SAVE_DIR = "saved_frames"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# Background subtractor for motion detection
bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=250, varThreshold=16, detectShadows=True)

# Dictionary to keep track of frame counts for each user
frame_counters = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_frame', methods=['POST'])
def upload_frame():
    # Get username from request headers (or query parameters)
    username = request.form.get('username', 'unknown_user')
    user_folder = os.path.join(SAVE_DIR, username)
    
    # Ensure user-specific folder exists
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)
    
    # Initialize frame counter for the user if not already done
    if username not in frame_counters:
        frame_counters[username] = 0
    
    # Get the image from the request
    file_bytes = np.frombuffer(request.files['image'].read(), np.uint8)
    frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Apply background subtraction to detect motion
    fg_mask = bg_subtractor.apply(frame)
    mean_diff = np.mean(fg_mask)
    
    # Increment the frame counter
    frame_counters[username] += 1
    frame_num = frame_counters[username]

    # Save frame if motion is detected
    if mean_diff > 5:  # You can adjust this threshold
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        file_path = os.path.join(user_folder, f"frame_{frame_num}_{timestamp}.jpg")
        cv2.imwrite(file_path, frame)
        print(f"Saved frame: {file_path}")

    return "Frame received", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context=('cert.pem', 'key.pem'))
