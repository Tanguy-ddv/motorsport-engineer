from .client import Client
from .server import Server
from utils.constant import SERVER_IP, SERVER_PORT
network_server = Server(SERVER_IP, SERVER_PORT)
__all__ = ['Client', 'network_server']