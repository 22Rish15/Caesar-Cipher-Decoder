from email import message
import socket

msg = input("Please enter your meesage : \n")
key = "abcdefghijklmnopqrstuvwxyz0123456789 !@#";
val = key[::-1];
enc = dict(zip(key,val));
message = "".join([enc[words] for words in msg.lower()])


s= socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
s.bind((socket.gethostname(),32120))

s.listen(5)
while True:
    clt,adr = s.accept()
    
    clt.send(bytes(message,"utf-8"))
