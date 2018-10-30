from kazoo.client import KazooClient


class ZookeeperClient():

    def __init__(self, zookeeper_address):
        '''
        Class variable will be initialized here
        '''
        self.address = zookeeper_address
