import socket 
s = socket.socket()
s.connect(('localhost', 9000))
while True:
    ip = input("Enter the MAC address: ")
    s.send(ip.encode())
    print("Logical Address", s.recv(1024).decode())