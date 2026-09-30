import threading
import multiprocessing
import queue
import time


# Threading
def threading_demo():
    q = queue.Queue()

    def producer():
        for i in range(1, 6):
            q.put(i)
            print("Produced:", i)

    def consumer():
        for i in range(1, 6):
            item = q.get()
            print("Consumed:", item)

    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


# Multiprocessing
def producer(q):
    for i in range(1, 6):
        q.put(i)
        print("Process Produced:", i)


def consumer(q):
    for i in range(1, 6):
        item = q.get()
        print("Process Consumed:", item)


if __name__ == "__main__":

    print("Threading:")
    threading_demo()

    print("\nMultiprocessing:")

    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
