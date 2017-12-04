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

    def isValidUsername(self):
        #check for uppercase letters
        hasUpper = False;
        for c in self.username:
            hasUpper = c.isupper();
            if hasUpper:
                break;
                
        if(not hasUpper):
            return False;

        # check lower case
        hasLower = False;
        for c in self.username:
            hasLower = c.islower();
            if hasLower:
                break;
                
        if not hasLower:
            return False;

        # check digit
        hasDigit = False;
        for c in self.username:
            hasDigit = c.isdigit();
            if hasDigit:
                break;
                
        if not hasDigit:
            return False;

        hasSymbol = False;
        symbols = ['.', '-', '_'];
        for c in self.username:
            for s in symbols:
                if c is s:
                    hasSymbol = True;
                    break;
            if hasSymbol:
                break;

        if not hasSymbol:
            return False;

        return True;
