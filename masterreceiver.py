from queue import Queue, Empty
from threading import Thread
import socket;

class MasterReceiver(Thread):
    def __init__(self, socket, hQueue, crQueue):
        Thread.__init__(self);
        self.socket = socket;
        self.hQueue = hQueue;
        self.crQueue = crQueue;
        self.bufferLength = 1024;
        
    def run(self):
        while True:
            data, addr = self.socket.recvfrom(self.bufferLength);
            msg = data.decode();
            if self.isHelloMsg(msg):
                msg = msg[5:];
                self.hQueue.put((msg, addr));
            else: 
                self.crQueue.put((msg, addr));

    def isHelloMsg(self, msg):
        index = msg.find("HELLO");
        if(index == 0):
            return True;

        return False;
            
