
import bittensor
import pickle

import grpc
import time
import metagraph_pb2
import metagraph_pb2_grpc

if __name__ == '__main__':

    # Connections.
    channel = grpc.insecure_channel( '167.172.139.4:7869' )
    stub = metagraph_pb2_grpc.MetagraphServerStub( channel )
    request = metagraph_pb2.Block ()
    graph = bittensor.metagraph()
    start = time.time()
    state = pickle.loads(stub.Get( request = request ).bytes)
    print (state)
    graph.load_from_state_dict( state )
    print( graph )
    print( time.time() - start)





