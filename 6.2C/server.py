import socket

dns_table = {
    "www.google.com": "192.168.1.1",
    "www.facebook.com": "192.168.1.3",
    "www.spotify.com": "192.168.1.4",
    "www.canva.com": "192.168.1.5",
    "www.youtube.com": "192.168.1.6",
    "www.w3school.com": "192.168.1.7"
}

cname_record = {
    "www.google.com": "host.google.com",
    "www.facebook.com": "host.facebook.com",
    "www.spotify.com": "host.spotify.com",
    "www.canva.com": "host.canva.com",
    "www.youtube.com": "host.youtube.com",
    "www.w3school.com": "host.w3school.com"
}

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server is running")

# Get IP address of the server
ip_address = socket.gethostbyname(socket.gethostname())
print("Server IP address:", ip_address)

clientSocket.bind(("127.0.0.1", 9992))

while True:
    data, address = clientSocket.recvfrom(1024)
    message = format(address) + " requested to fetch data"
    print(message)

    data = data.decode()
    ip = dns_table.get(data, "Data not found").encode()
    cname = cname_record.get(data, "none").encode()

    send = clientSocket.sendto(ip, address)
    send1 = clientSocket.sendto(cname, address)
