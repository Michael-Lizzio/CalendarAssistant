import threading


class Counter:
    def __init__(self, start_count: int = 0):
        self.lock = threading.Lock()
        self.count = start_count
        self.done = False

    def add_to_count(self):
        with self.lock:
            self.count += 1

    def is_done(self):
        return self.done

    def set_done(self, done):
        self.done = done

    def get_count(self):
        return self.count
