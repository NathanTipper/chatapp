from threading import Timer;

class Peer:
    def __init__(self, username = "", addr = 0, port = 0):
        self.username = username;
        self.addr = addr;
        self.port = port;
    
    def areEqual(self,peer):
        if self.username != peer.username:
            return False;
        if self.addr != peer.addr:
            return False;
        if self.port != peer.port:
            return False;
            
        return True;
    
    def printInfo(self):
        print(("\n{} : {} : {}").format(self.username, self.addr, self.port));
