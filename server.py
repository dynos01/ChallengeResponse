import json
import string
import random
from md5 import md5
from xmlrpc.server import SimpleXMLRPCServer

bindAddr = "127.0.0.1"
bindPort = 2333
userData = "users.json"

class serverObj:
    challenge = ""
    def getChallenge(self):
        charSet = string.ascii_letters + string.digits + string.punctuation
        self.challenge = "".join(random.choice(charSet) for i in range(16))
        return self.challenge
    def getStatus(self, username, message):
        with open(userData) as f:
            data = json.load(f)
        for i in data:
            if i["username"] == username:
                message0 = md5(self.challenge + i["username"] + i["key"])
                if message == message0:
                    return True
                return False
        return False

def main():
    server = SimpleXMLRPCServer((bindAddr, bindPort))
    serverInstance = serverObj()
    server.register_instance(serverInstance)
    server.serve_forever()

if __name__ == "__main__":
    main()
