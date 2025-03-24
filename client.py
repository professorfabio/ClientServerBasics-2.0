from socket  import *
from constCS import * #-
import pickle

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
op = input("Operation to invoke: ")
v1 = int(input("Enter 1st operand: "))
v2 = int(input("Enter 2nd operand: "))
data = {"OP":op, "V1":v1, "V2":v2}
msg = pickle.dumps(data)
#packet = str.encode(msg)
s.send(msg)  # send data packet
msg = s.recv(1024)     # receive the response
#msg = bytes.decode(packet)
data = pickle.loads(msg)
print ("Result: ", data)            # print the result
s.close()               # close the connection
