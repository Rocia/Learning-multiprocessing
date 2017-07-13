from multiprocessing import Process, Queue
from multiprocessing.managers import BaseManager
class Worker(Process):
    def __init__(self, q):
        self.q = q
        super(Worker, self).__init__()
    def run(self):
        self.q.put('local hello')
queue = Queue()
w = Worker(queue)
w.start()
class QueueManager(BaseManager): pass
QueueManager.register('get_queue', callable=lambda: queue)
m = QueueManager(address=('', 50000), authkey='abracadabra')
s = m.get_server()
s.serve_forever()
