import random
import threading
import time

from counter import Counter


class Adders:
    COUNT_TO = 10

    def __init__(self, counter: Counter, counter_count=5):
        self.counter_count = counter_count
        self.counter = counter

    def counter_printer(self):
        while True:
            count = self.counter.get_count()
            print(count)
            time.sleep(.5)
            if self.counter.is_done():
                break

    def start_counter(self, counter_id: int):
        print(f"Counter {counter_id} starting!")
        for i in range(self.COUNT_TO):
            self.counter.add_to_count()
            print(f"Counter {counter_id} added to count!")
            time.sleep(random.randint(0, 3))

    def start_thread_counters(self):
        threads = []
        for i in range(self.counter_count):
            thread = threading.Thread(target=self.start_counter, args=(i,))
            thread.start()
            threads.append(thread)

        counter_thread = threading.Thread(target=self.counter_printer)
        counter_thread.start()

        for thread in threads:
            thread.join()

        counter.set_done(True)

        counter_thread.join()
        print("Success")


if __name__ == '__main__':
    counter = Counter()
    adders = Adders(counter, 10)
    adders.start_thread_counters()
