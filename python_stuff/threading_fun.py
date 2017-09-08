import threading

total = 0
lock = threading.Lock()


def update_total(amount):
    """
    update the global variable 'total'
    """

    global total
    lock.acquire()
    try:
        total += amount
    finally:
        lock.release()
    print(total)

if __name__ == '__main__':
    for i in range(10):
        my_thread = threading.Thread(target=update_total, args=(5,))
        my_thread.start()

