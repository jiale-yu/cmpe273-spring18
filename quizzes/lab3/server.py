import zmq

context = zmq.Context()

#req/rep pattern setup
get_msg_sock = context.socket(zmq.REP)
get_msg_sock.bind("tcp://127.0.0.1:5679")

#pub/sub pattern setup
broadcast_sock = context.socket(zmq.PUB)
broadcast_sock.bind("tcp://127.0.0.1:5680")
print("Server started...")
while 1:
    message = get_msg_sock.recv()
    message = message.decode('utf-8')
    get_msg_sock.send_string("\n")
    print(message)
    broadcast_sock.send_string(message)