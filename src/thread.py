from itertools import cycle
from time import sleep
import sys
from threading import Thread
import src.opening as opening

class Spin(Thread):
    """Thread to print a spinning wheel on stdout while a task is ongoing"""

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        """Display the spinning wheel when the thread is running"""
        while opening.working:
            for frame in cycle(r'-\|/-\|/'):
                print('*\r*', frame, sep='', end='', flush=True)
                if opening.working == 0: break
                sleep(0.2)
