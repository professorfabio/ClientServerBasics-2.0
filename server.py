from socket  import *
from threading import Thread
import pickle
from random import *
from constCS import * #-

def execute(data, num):
  print ("Thread: ", num)
  if data["OP"] == "sum":
    res = data["V1"] + data["V2"]
    status = "OK"
  elif data["OP"] == "sub":
    res = data["V1"] - data["V2"]
    status = "OK"
  else:
    status = "NOK"
    res = 1
  data = {"STATUS":status, "RES":res}
  msg = pickle.dumps(data)
  conn.send(msg)
  return

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-

while True:                # forever
  (conn, addr) = s.accept()  # returns new socket and addr. client 
  msg = conn.recv(1024)    # receive data from client
  if msg: 
    print(msg)
    data = pickle.loads(msg)
    print(data)
    if data["OP"] == "fim":
      data = {"STATUS":"FIM","RES":0}
      msg = pickle.dumps(data)
      conn.send(msg)
      break
    else:
      num = randint(1,100)
      t = Thread (target=execute, args=(data,num))
      t.start()
conn.close()               # close the connection
