import concurrent.futures
import time

class Server:
    def __init__(self):
        thread_count = 2
        executor = concurrent.futures.ProcessPoolExecutor(thread_count)

        while 1:
            futures = [executor.submit(self.main_loop) for thread in range(0, thread_count-1)]
            concurrent.futures.wait(futures)
            time.sleep(0.2)

    def main_loop(self):
        print("1")

if __name__ == '__main__':
    Server()
