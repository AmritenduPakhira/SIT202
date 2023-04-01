import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get local machine name
host = socket.gethostname()

port = 9999

while True:
    # send some data to the server
    message = 'Hello Server'
    client_socket.sendto(message.encode(), (host, 9999))

    # receive a response from the server
    data, addr = client_socket.recvfrom(1024)
    print('Received response from server: {}'.format(data.decode()))

    inp = input('Enter your name: ')
    client_socket.sendto(inp.encode(), (host, 9999))

    print('Hello ' + str(inp) + ', Welcome to SIT-202!')

    input1 = input('Do you want to continue (y/n)? ')

    if input1.lower() == 'y':
        inp1 = input('Enter your name: ')
        client_socket.sendto(inp1.encode(), (host, 9999))
        print('Hello ' + str(inp1) + ', Welcome to SIT-202!')
    elif input1.lower() == 'n':
        print('Program ended. Thank you.')
        break
    else:
        print('Invalid Response!')
        break

client_socket.close()
