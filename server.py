from socket  import *
from constCS import * #-
import pickle

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
  msg = conn.recv(1024)    # receive data from client
  if not msg: break        # stop if client stopped
  #msg = bytes.decode(packet) 
  print(msg)
  data = pickle.loads(msg)
  print(data)
  if data["OP"] == "sum":
    data = data["V1"] + data["V2"]
    msg = pickle.dumps(data)
    #packet = str.encode(msg)
    conn.send(msg)
conn.close()               # close the connection
