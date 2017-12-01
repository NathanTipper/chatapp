import socket;
import threading;
import sys;
import os;
import random;
import time;
from peerdiscover import PeerDiscover;
from peer import Peer;
from masterreceiver import MasterReceiver;
from messenger import Messenger;
from broadcaster import Broadcaster;
from queue import Queue, Empty;

PORT_MIN = 50000;
PORT_MAX = 50008;

def main():
        if len(sys.argv) != 2:
                print("Usage: {} [username]".format(sys.argv[0]));
                sys.exit(1);

        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
        except:
                print('Could not create socket');
                exit(1);
        
        port = PORT_MIN;
        while True:
                try:
                        s.bind(('', port));
                        break;
                except:
                        print('Could not bind socket');
                        port += 1;
                        if(port > PORT_MAX):
                                exit(1);


        hQueue = Queue();
        crQueue = Queue();
        csQueue = Queue();
        peerList = [];
        bc = Broadcaster(s, peerList, sys.argv[1]);
        mr = MasterReceiver(s, hQueue, crQueue);
        pd = PeerDiscover(peerList, hQueue);
        mgr = Messenger(s, peerList, crQueue, csQueue);

        bc.daemon = True;
        mr.daemon = True;
        pd.daemon = True;
        mgr.daemon = True;
    
        bc.start();
        mr.start();
        pd.start();
        mgr.start();
	
        #print("Loading peers...");
	
        msg = "";
        while True:
                msg = input(sys.argv[1] + ": ");
                if len(msg) == 1 and msg[0] == 'q':
                        break;
                if(msg == "list"):
                        print(" Users online: ");
                        for i in range(0, len(peerList)):
                                print(peerList.username);
                csQueue.put(msg);
	
        print("Logged off");
	
main();
