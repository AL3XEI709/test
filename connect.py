import socket 
class Aleksei(): 
    def __init__(self,host,port): 
        self.host = host 
        self.port = port 

    def connect(self):
        out = (self.host,self.port) 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(out) 
        return sock 


def recvutil(aim,bintext):
    out=b''
    while True:
        rec = aim.recv(1024) 
        if bintext in rec:
            out += rec   
            return out  
        out += rec
    
