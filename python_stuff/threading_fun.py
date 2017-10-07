# coding=utf-8
"""Just experimenting with Pycharm's concurrency diagram"""

import time
import threading
import random


class AwesomeThreading(threading.Thread):
    """
    Threading is awesome still
    """

    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.duration = random.randint(5, 5)
        self.thread_name = thread_name

    def run(self):
        """
        slightly customized newly created threads to block for some seconds
        """
        print(f'Starting {self.thread_name} {time.ctime(time.time())}')
        print(f'Locking thread {self.thread_name} for {self.duration} seconds')
        thread_lock.acquire()  # both threads will start together, but thread 2 will end with a 5 seconds delay
        # because thread1 was blocking for 5 seconds.
        time.sleep(self.duration)
        print(f'Ending {self.thread_name} {time.ctime(time.time())}')
        thread_lock.release()

    def exact_time(self, action):
        print(f'{self.thread_name}: {time.ctime(time.time())}')


thread_lock = threading.Lock()
threads = []

thread1 = AwesomeThreading('Thread 1')
thread2 = AwesomeThreading('Thread 2')

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for thread in threads:
    thread.join()

print("Main thread work is done for this part")

"""
pydev debugger: process 9928 is connecting

Connected to pydev debugger (build 172.3968.37)
Starting Thread 1 Sat Oct  7 13:08:59 2017
Locking thread Thread 1 for 5 seconds
Starting Thread 2 Sat Oct  7 13:08:59 2017
Locking thread Thread 2 for 5 seconds
Ending Thread 1 Sat Oct  7 13:09:04 2017
Ending Thread 2 Sat Oct  7 13:09:09 2017
Main thread work is done

Process finished with exit code 0
"""