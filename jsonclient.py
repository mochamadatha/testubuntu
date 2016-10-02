import socket
import json

def Main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect( ('127.0.0.1', 4000) )

    message = raw_input("Nama File (Beserta .json) : ")
    while message != 'q':
            with open(message) as f:
		json_data = json.load(f)
	    datajs = json.dumps(json_data)
	    sock.send(datajs)
            message = raw_input("Nama File (Beserta .json) : ")
    sock.close()
if __name__== '__main__':
    Main()
