
import bittensor
import pickle
from concurrent import futures

import grpc
import time
import metagraph_pb2
import metagraph_pb2_grpc

class MetagraphServicer ( metagraph_pb2_grpc.MetagraphServer ):
    def __init__(self):
        graph = bittensor.metagraph( network = 'akatsuki')
        # graph.load()
        self.bytes = pickle.dumps( graph.state_dict() )

    def Get( self, request: metagraph_pb2.Block, context: grpc.ServicerContext  ) -> metagraph_pb2.Metagraph:
        return metagraph_pb2.Metagraph ( bytes = self.bytes )

if __name__ == '__main__':

    # Create server.
    thread_pool = futures.ThreadPoolExecutor( max_workers = 10 )
    metagraph_server = grpc.server( thread_pool )
    metagraph_servicer = MetagraphServicer()
    metagraph_pb2_grpc.add_MetagraphServerServicer_to_server( metagraph_servicer, metagraph_server )
    metagraph_server.add_insecure_port( '127.0.0.1:7869' )
    metagraph_server.start()

    print ('starting loop:')
    while True:
        print ('heartbeat.')
        time.sleep(1)

    # # Connections.
    # channel = grpc.insecure_channel( '127.0.0.1:7869' )
    # stub = metagraph_pb2_grpc.MetagraphServerStub( channel )
    # request = metagraph_pb2.Block ()
    # graph = bittensor.metagraph()
    # state = pickle.loads(stub.Get( request = request ).bytes)
    # graph.load_from_state_dict( state )
    # print( graph )





