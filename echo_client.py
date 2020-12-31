import socket
import sys
import traceback


def client(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 10000)
    # TODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    print('       CLIENT connecting to {0} port {1}'.format(*server_address), file=log_buffer, flush=True)
    # TODO: connect your socket to the server here.
    sock.connect(("127.0.0.1", 10000))
    # you can use this variable to accumulate the entire message received back
    # from the server
    received_message = ''

    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it
    try:
        print('       CLIENT sending "{0}"'.format(msg), file=log_buffer, flush=True)
        # TODO: send your message to the server here.
        # message = input("Hello World! Hello World! Hello World!")
        sock.sendall(msg.encode('utf-8'))
        # TODO: the server should be sending you back your message as a series
        #       of 16-byte chunks. Accumulate the chunks you get to build the
        #       entire reply from the server. Make sure that you have received
        #       the entire message and then you can break the loop.
        while True:
            chunk = sock.recv(16) # client
            if not chunk:
                print("       CLIENT not chunk", file=log_buffer, flush=True)
                break
            #       Log each chunk you receive.  Use the print statement below to
            #       do it. This will help in debugging problems
            received_message += chunk.decode('utf8') 
            print('       CLIENT received "{0}"'.format(chunk.decode('utf8')), file=log_buffer, flush=True)
            chunk = '' # empty the chunk so we can use it again
            print(f'       CLIENT accumulated: "{received_message}"', file=log_buffer, flush=True)
        return received_message
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
    finally:
        # TODO: after you break out of the loop receiving echoed chunks from
        #       the server you will want to close your client socket.
        print('       CLIENT closing socket', file=log_buffer, flush=True)
        sock.close()
        # TODO: when all is said and done, you should return the entire reply
        # you received from the server as the return value of this function.
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
