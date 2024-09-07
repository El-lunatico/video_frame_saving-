# Flask Motion Detection Frame Saver

This Flask application allows users to upload frames via an HTML web interface. The frames are processed to detect motion using background subtraction. If motion is detected, the frame is saved to a user-specific directory. Additionally, a QR code is generated to provide a link to the running Flask server.

## Features

- HTML interface to start and stop camera streaming.
- Upload frames via a form in the web interface.
- Detect motion in uploaded frames using background subtraction.
- Save frames with detected motion to user-specific directories.
- Generate a QR code with the server's IP address and port.

## Requirements

- Python 3.6 or higher
- Flask
- OpenCV
- NumPy
- qrcode

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install Flask opencv-python numpy qrcode
    ```

4. (Optional) Generate SSL certificates:

    Ensure you have `cert.pem` and `key.pem` in the root directory. If you don't have SSL certificates, you can remove the `ssl_context` parameter from the `app.run()` call.

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Access the application by scanning the QR code displayed in the terminal or by navigating to `http://<IP_ADDRESS>:5000` in your web browser. Replace `<IP_ADDRESS>` with the IP address displayed in the QR code.

3. Open the web interface in your browser. You'll see an input field for entering your username and buttons to start and stop the camera.

4. Click "Start Camera" to access your webcam and begin capturing frames. Enter your username before starting the camera.

5. The camera will capture frames every second and send them to the server. If motion is detected in a frame, the frame will be saved in a directory specific to your username.

6. Click "Stop Camera" to stop capturing frames and stop the webcam.

## HTML Interface

- **Username Input**: Enter your username in the text field provided.
- **Start Camera Button**: Starts the camera and begins capturing frames.
- **Stop Camera Button**: Stops the camera and stops frame capture.
- **Video Element**: Displays the webcam feed when the camera is active.

## Directory Structure

- `app.py`: The main Flask application script.
- `saved_frames/`: Directory where frames are saved.
- `templates/index.html`: HTML file for the web interface.
- `cert.pem` (optional): SSL certificate file.
- `key.pem` (optional): SSL key file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)
- [qrcode](https://pypi.org/project/qrcode/)
- [WebRTC](https://webrtc.org/)

