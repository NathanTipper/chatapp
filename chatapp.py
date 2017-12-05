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

PORT_MIN = 55000;
PORT_MAX = 55008;


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
                        port += 1;
                        if(port > PORT_MAX):
                                print("Could not bind socket");
                                exit(1);

        # get user info
        addrinfo = socket.getaddrinfo(socket.gethostname(), port);
        addressFam = addrinfo[2];
        addr = addressFam[4];

        # make local peer
        localPeer = Peer(sys.argv[1], addr[0], addr[1]);
        while(not localPeer.isValidUsername()):
                newUsername = input("Please enter a username with at least one upper letter, one lower letter, one digit, and one of .-_: ");
                localPeer = Peer(newUsername, addr[0], addr[1]);
        
        hQueue = Queue();
        crQueue = Queue();
        csQueue = Queue();
        peerList = [];
        peerList.append(localPeer);
        bc = Broadcaster(s, peerList);
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
                msg = input(localPeer.username + ": ");
                if len(msg) == 1 and msg[0] == 'q':
                        break;
                elif(msg == "list"):
                        print(" Users online: ");
                        for i in range(1, len(peerList)):
                                print(peerList[i].username);
                        continue;
                elif len(msg) == 1 and msg[0] == 'p':
                        peerList[0].printInfo();
                        continue;

                csQueue.put(msg);
	
        print("Logged off");
	
main();
