import socket

host_name = socket.gethostname()
port = 5000

c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c_socket.connect((host_name, port))

msg = input(" -> ")

while msg.lower().strip() != 'bye':
    c_socket.sendall(msg.encode())
    recv_data = c_socket.recv(1024).decode()
    print("Received from server: " + recv_data)

    msg = input(" -> ")

c_socket.close()
