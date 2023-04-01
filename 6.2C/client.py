import socket

clientAddr = "127.0.0.1"
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = (clientAddr, 9992)

user_decision = "Y"

user_name = input("Please enter your name: ")
print("Welcome, " + user_name + " to SIT202 Network Communication.")

while user_decision.upper() == "Y":
    domain_input = input("Enter domain name for which the IP is needed: ")
    send = clientSocket.sendto(domain_input.encode(), addr)

    data, address = clientSocket.recvfrom(1024)
    cname, address = clientSocket.recvfrom(1024)

    server_reply = data.decode().strip()
    cname_reply = cname.decode().strip()
    message = "The IP for the " + format(cname_reply) + " server is " + format(server_reply)
    print(message)

    user_decision = input("Do you want to continue? (Y/N) ")

    if user_decision.upper() != "Y":
        print("Program ended. Thank you.")
        break

clientSocket.close()





