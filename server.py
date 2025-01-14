import socket

def server_start():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # set up socket connection
    server_address = ('localhost', 10000)
    sock.bind(server_address)

    # listen for incoming connections
    sock.listen(1)


def grab_livestream():

# empty
if __name__ ==  "__main__":
    server_start()