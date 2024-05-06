import socket
import pyautogui

# Set up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 5555))
server_socket.listen(1)

print("Server listening on port 5555")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

while True:
    # Receive command from client
    command = client_socket.recv(1024).decode()

    if command == "screenshot":
        # Capture screenshot
        screenshot = pyautogui.screenshot()

        # Send screenshot size to the client
        size = screenshot.size
        client_socket.send(str(size).encode())

        # Send screenshot data
        screenshot_bytes = screenshot.tobytes()
        client_socket.sendall(screenshot_bytes)

    elif command == "exit":
        break

# Close the connection
client_socket.close()
server_socket.close()
