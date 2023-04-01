import socket
# create a socket object

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind the socket to a public host, and a well-known port
server_socket.bind((host, port))

print('Waiting for a client to connect...')
while True:
    # receive data from the client
    data, addr = server_socket.recvfrom(1024)
    message = data.decode()
    print('Received data from client: {}'.format(message))

    # send a response back to the client
    response = 'Hello, please tell your first name'
    server_socket.sendto(response.encode(), addr)

    inp, addr = server_socket.recvfrom(1024)
    name = inp.decode()

    print('Name of the client is: ' + name)
    server_socket.sendto(response.encode(), addr)
