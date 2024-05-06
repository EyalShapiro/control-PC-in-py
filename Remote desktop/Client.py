import socket
from PIL import Image

# Set up client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("server_ip_address", 5555))

while True:
    # Send command to server
    command = input("Enter command (screenshot/exit): ")
    client_socket.send(command.encode())

    if command == "screenshot":
        # Receive screenshot size
        size = tuple(map(int, client_socket.recv(1024).decode().split(",")))

        # Receive screenshot data
        screenshot_data = client_socket.recv(1024)
        while len(screenshot_data) < size[0] * size[1] * 3:
            screenshot_data += client_socket.recv(1024)

        # Display the screenshot
        screenshot = Image.frombytes("RGB", size, screenshot_data)
        screenshot.show()

    elif command == "exit":
        break

# Close the connection
client_socket.close()
