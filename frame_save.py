import os
import cv2
import numpy as np
import re
from flask import Flask, render_template, request, jsonify, send_from_directory
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
    # Get username and session_id from request
    username = request.form.get('username', 'unknown_user')
    session_id = request.form.get('session_id', 'default_session')
    
    # Sanitize session_id to remove invalid characters
    session_id = re.sub(r'[<>:"/\\|?*]', '', session_id)
    
    user_folder = os.path.join(SAVE_DIR, username)
    session_folder = os.path.join(user_folder, session_id)
    
    try:
        # Ensure user-specific folder and session folder exist
        os.makedirs(session_folder, exist_ok=True)
        
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
            file_path = os.path.join(session_folder, f"frame_{frame_num}_{timestamp}.jpg")
            cv2.imwrite(file_path, frame)
            print(f"Saved frame: {file_path}")
        
        return "Frame received", 200
    
    except Exception as e:
        print(f"Error saving frame: {e}")
        return "Error saving frame", 500

@app.route('/get_frames', methods=['GET'])
def get_frames():
    username = request.args.get('username', 'unknown_user')
    session_id = request.args.get('session_id', 'default_session')
    
    # Sanitize session_id to remove invalid characters
    session_id = re.sub(r'[<>:"/\\|?*]', '', session_id)
    
    user_folder = os.path.join(SAVE_DIR, username)
    session_folder = os.path.join(user_folder, session_id)
    
    if not os.path.exists(session_folder):
        return jsonify([])  # No frames if session folder does not exist
    
    try:
        frames = []
        for filename in os.listdir(session_folder):
            if filename.endswith('.jpg'):
                file_path = os.path.join(session_folder, filename)
                # Construct the URL for the image
                frames.append({'url': f'/frames/{username}/{session_id}/{filename}'})
        
        return jsonify(frames)
    
    except Exception as e:
        print(f"Error retrieving frames: {e}")
        return jsonify([])

@app.route('/frames/<username>/<session>/<filename>')
def serve_frame(username, session, filename):
    directory = f'D:/Algoristan_Internship/python/saved_frames/{username}/{session}'
    return send_from_directory(directory, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context=('cert.pem', 'key.pem'))
