from socket  import *
from constCS import * #-
import pickle

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
  packet = conn.recv(1024)    # receive data from client
  if not packet: break        # stop if client stopped
  msg = bytes.decode(packet) 
  print(msg)
  data = pickle.loads(msg)
  print(data)
  if data[0] == "SUM":
    data = data[1] + data[2]
    msg = pickle.dumps(data)
    packet = str.encode(msg)
    conn.send(packet)
conn.close()               # close the connection
