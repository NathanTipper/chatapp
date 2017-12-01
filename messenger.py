from queue import Queue, Empty;
from threading import Thread;
import socket;

class Messenger(Thread):
    def __init__(self, socket, peerList, crQueue, csQueue):
        self.socket = socket;
        self.peerList = peerList;
        self.crQueue = crQueue;
        self.csQueue = csQueue;

    def run():
        while True:
            try:
                msg, addr = self.crQueue.get(False);
                peer = findPeer(addr);
                print(peer.username + ": " + msg);
			
			except Queue.Empty:
				# do nothing
			
            except Exception as error:
                print(repr(error));

            try:
				msg = self.csQueue.get(False);
                for i in range(0, len(peerList)):
					addr = peerList[i].addr;
					port = peerList[i].port;
					self.socket.sendto(msg.encode(), (addr, port));
					
            except Queue.Empty:
				# do nothing
                
    def findPeer(addr):
        for i in range(0, len(peerList)):
            if addr[0] != peerList[i].addr:
                continue;
            elif addr[1] != peerList[i].port:
                continue;

            return peerList[i];

        raise Exception("Could not find peer in list!");
