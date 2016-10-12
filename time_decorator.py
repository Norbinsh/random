# Very basic decorator to caltulate the time it took for the function to run

import time

current_time_in_mili = lambda: int(round(time.time() * 1000))


def time_decorator(function):
    def timed(*args, **kw):
        start = current_time_in_mili()
        result = function(*args, **kw)
        end = current_time_in_mili()

        print(function.__name__, args[0], kw, end-start)
        return result
    return timed

class Cnt(object):
    @time_decorator
    def poo(self, b=4, c=5):
        time.sleep(0.5)
    @time_decorator
    def print_to_x(self, x):
        print(x)
        print([i for i in range(0, x)])
        time.sleep(1)

Cnt.print_to_x(Cnt, 50)



