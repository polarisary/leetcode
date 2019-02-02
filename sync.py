import threading

alock = threading.Lock()
block = threading.Lock()
cond = threading.Condition()

class A(threading.Thread):
    def run(self):
        cond.acquire()
        for i in range(1, 100, 2):
            # block.acquire()
            print('A ' + str(i))
            # alock.release()
            cond.notify()
            cond.wait(1)
        cond.notify()
        cond.release()

class B(threading.Thread):
    def run(self):
        cond.acquire()
        cond.wait(1)
        for i in range(2, 100, 2):
            # alock.acquire()
            print('B ' + str(i))
            # block.release()
            cond.notify()
            cond.wait(1)
        cond.notify()
        cond.release()

if __name__ == "__main__":
    a = A()
    b = B()
    # alock.acquire()
    b.start()
    a.start()
    a.join()
    b.join()