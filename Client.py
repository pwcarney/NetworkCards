import socket
import sys


class Client:
    def __init__(self):
        host = 'localhost'
        port = 8888

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket created')

        try:
            s.bind((host, port))
        except socket.error as msg:
            print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()

        print('Socket bind complete')

        s.listen(10)
        print('Socket now listening')

        # now keep talking with the client
        while 1:
            # wait to accept a connection - blocking call
            conn, addr = s.accept()
            print('Connected with ' + addr[0] + ':' + str(addr[1]))

        s.close()

if __name__ == '__main__':
    Client()
