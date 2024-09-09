# Motion-Based Frame Capture System

## Overview

This project is a web-based application designed to capture and save video frames based on motion detection. The system streams video from the user's camera and transmits frames to a Flask server, which processes and stores frames when motion is detected using background subtraction techniques. The application offers features to control camera functions, including starting/stopping the camera, flipping between front and rear cameras, and managing recording timers.

## Features

- **Live Camera Streaming**: View real-time video feed directly on the webpage.
- **Camera Control**: Start and stop the camera feed with dedicated buttons.
- **Camera Flip**: Switch between front and rear cameras.
- **Recording Timer**: Manage recording with a visible countdown timer.
- **Frame Capture and Transmission**: Automatically capture and send frames to the server at regular intervals.
- **Motion Detection**: Employ background subtraction to identify and save frames when motion is detected.

## Requirements

- Modern web browser (Chrome, Firefox, Edge)
- Python 3.x
- Flask
- OpenCV

## Setup

### Frontend

1. **Create `index.html`**

   Save the provided HTML file as `index.html` in your project directory.

### Backend

1. **Install Dependencies**

    Ensure Flask and OpenCV are installed. Use the following command to install them:

    ```bash
    pip install flask opencv-python
    ```

2. **Create `server.py`**

    Save the provided Python code as `server.py` in your project directory.

3. **Generate SSL Certificates (Optional)**

    To enable SSL (https) for secure connections, generate your SSL certificates (`cert.pem` and `key.pem`) and place them in the project directory. For local testing, you may skip the `ssl_context` parameter in the `app.run()` method.

4. **Run the Flask Server**

    ```bash
    python server.py
    ```

5. **Open the HTML File**

    Open `index.html` in your web browser to interact with the application.

## How It Works

1. **Client-Side (HTML/JavaScript)**

    - Users input their username and activate the camera.
    - The application captures frames every 100ms and sends them to the server.
    - Users can toggle between front and rear cameras and stop recording as needed.

2. **Server-Side (Flask)**

    - The server processes incoming frames and saves them when motion is detected using background subtraction.
    - Frames are organized and stored in user-specific directories with timestamps.

## Notes

- Ensure that your browser permits camera access.
- The timer and frame capture intervals are set to 15 seconds and 100ms, respectively, and can be customized in the HTML script section.
- Adjust the motion detection sensitivity threshold in `server.py` according to your requirements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
