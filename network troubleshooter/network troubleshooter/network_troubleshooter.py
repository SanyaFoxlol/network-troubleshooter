import socket
import os

print("Hostname:", socket.gethostname())
print("IP:", socket.gethostbyname(socket.gethostname()))

os.system("ping google.com")
