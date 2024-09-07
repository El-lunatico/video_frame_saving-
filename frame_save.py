import os
import cv2
import numpy as np
from flask import Flask, render_template, request
import time
import qrcode
import socket


app = Flask(__name__)
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(("8.8.8.8", 80))
        ip=s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'

    return ip

# Directory to save frames
SAVE_DIR = "saved_frames"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# Background subtractor for motion detection
bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)

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
    
    # Get the image from the request
    file_bytes = np.frombuffer(request.files['image'].read(), np.uint8)
    frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Apply background subtraction to detect motion
    fg_mask = bg_subtractor.apply(frame)
    mean_diff = np.mean(fg_mask)
    
    # Save frame if motion is detected
    if mean_diff > 10:  # You can adjust this threshold
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        file_path = os.path.join(user_folder, f"frame_{timestamp}.jpg")
        cv2.imwrite(file_path, frame)
        print(f"Saved frame: {file_path}")

    return "Frame received", 200

if __name__ == "__main__":
    IP =get_ip()
    # The data you want to encode in the QR code
    data = f"http://{IP}:5000"

# Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
        box_size=4,  # size of each box in pixels
        border=4,  # thickness of the border
        )

# Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    qr.print_tty()
    # cert_path = os.path.join('D:', 'Algoristan_Internship', 'python', 'myenv', 'v_frame_on_flask', 'cert.pem')
    # key_path = os.path.join('D:', 'Algoristan_Internship', 'python', 'myenv', 'v_frame_on_flask', 'key.pem')
    app.run(host="0.0.0.0", port=5000,ssl_context=('cert.pem', 'key.pem') )


