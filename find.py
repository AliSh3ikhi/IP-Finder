import socket
import sys
add = sys.argv[1]
ip = socket.gethostbyname(add)

print('IP = ',ip)
