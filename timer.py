import time

class Timer:
    def __init__(self):
        self.t = 0

    def start(self):
        self.t = time.time()

    def end(self, msg):
        print(f"{msg}: {(time.time() - self.t):.2f}s")
