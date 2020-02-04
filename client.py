from md5 import md5
from xmlrpc.client import ServerProxy

serverURL = "http://127.0.0.1:2333"

def main():
    username = input("Username: ")
    key = input("Password: ")
    server = ServerProxy(serverURL)
    challenge = server.getChallenge()
    response = md5(challenge + username + key)
    status = server.getStatus(username, response)
    if status:
        print("Authentication successful")
    else:
        print("Authentication failure")

if __name__ == "__main__":
    main()
