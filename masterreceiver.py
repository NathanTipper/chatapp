from queue import Queue, Empty
from threading import Thread
import socket;

class MasterReceiver(Thread):
    def __init__(self, socket, hQueue, crQueue):
        self.socket = socket;
        self.hQueue = hQueue;
        self.crQueue = cQueue;
        self.bufferLength = 1024;
        
    def run():
        while True:
            data, addr = recvfrom(self.bufferLength);
            msg = data.decode();
            if isHelloMsg(msg):
                msg = msg[5:];
                self.hQueue.put((msg, addr));
            else 
                self.cQueue.put((msg, addr));
            

    def isHelloMsg(msg):
        index = msg.find("HELLO");
        if(index == 1):
            return True;

        return False;
            
