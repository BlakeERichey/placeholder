from blitzen.utils import get_local_ip
from blitzen.distributed import DistributedDispatcher

if __name__ == '__main__':
  ip = get_local_ip()
  dispatcher = DistributedDispatcher(server_ip=ip)
  dispatcher.spawn_server(duration=None)