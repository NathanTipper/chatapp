from queue import Queue, Empty;
from threading import Thread;
import socket;
import time;

class Messenger(Thread):
    def __init__(self, socket, peerList, crQueue, csQueue):
        Thread.__init__(self);
        self.socket = socket;
        self.peerList = peerList;
        self.crQueue = crQueue;
        self.csQueue = csQueue;

    def run(self):
        while True:
            try:
                msg, addr = self.crQueue.get(False);
                try:
                    peer = self.findPeer(addr);
                    print('\n' + peer.username + ": " + msg);
                except Exception as error:
                    print(str(error));
                    

            except Empty:
                continue;
            
            try:
                msg = self.csQueue.get(False);
                for i in range(1, len(self.peerList)):
                    addr = self.peerList[i].addr;
                    port = self.peerList[i].port;
                    self.socket.sendto(msg.encode(), (addr, port));
            except Empty:
                continue;

    def findPeer(self,addr):
        for i in range(1, len(self.peerList)):
            if addr[0] != self.peerList[i].addr:
                continue;
            elif addr[1] != self.peerList[i].port:
                continue;

            return self.peerList[i];

        raise Exception("Could not find peer in list!");
