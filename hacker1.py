from email import message
import socket

s= socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
s.connect((socket.gethostname(),32120))
message= s.recv(1000)
message= message.decode("utf-8")
 
print(message)
