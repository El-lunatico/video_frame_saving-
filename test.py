import os
print(f"Current Working Directory: {os.getcwd()}")
#     IP =get_ip()
#     # The data you want to encode in the QR code
#     data = f"http://{IP}:5000"

# # Create a QR code object
#     qr = qrcode.QRCode(
#         version=1,  # controls the size of the QR code
#         error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
#         box_size=2,  # size of each box in pixels
#         border=2,  # thickness of the border
#         )

# # Add data to the QR code
#     qr.add_data(data)
#     qr.make(fit=True)
#     qr.print_tty()
    # cert_path = os.path.join('D:', 'Algoristan_Internship', 'python', 'myenv', 'v_frame_on_flask', 'cert.pem')
    # key_path = os.path.join('D:', 'Algoristan_Internship', 'python', 'myenv', 'v_frame_on_flask', 'key.pem')

    # def get_ip():
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.settimeout(0)
    # try:
    #     s.connect(("8.8.8.8", 80))
    #     ip=s.getsockname()[0]
    # except Exception:
    #     ip = '127.0.0.1'

    # return ip