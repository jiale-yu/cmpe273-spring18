from __future__ import print_function

import grpc
import ping_pb2_grpc
from ping_pb2 import Request, Response


class PingClient():

    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:3000')
        self.stub = ping_pb2_grpc.PingPongStub(self.channel)

    def ping(self, data):
        req = Request(data=str(data))
        return self.stub.ping(req)


def run():
    client = PingClient()
    resp = client.ping("ping")
    print("Response = ",resp)


if __name__ == '__main__':
    run()