import socket
import datetime

UDP_IP = "192.168.1.185"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

file_name = "RSS Values.txt" # file name to write to
print("Writing to file: " + file_name)

f = open(file_name, "a")
f.write("\n New Write Started: " + str(datetime.datetime.now()) + "\n\n")

try:
  while True:
      data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
      f.write(str(data.decode("utf-8")) + "\n")

finally:
    f.close()

