import unittest
import threading
import time

num_threads = 4

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.num_threads

    def test_thread(self):



        def thread_message(message):
            num_threads -= 1
            print('Message from thread %s\n' %message)

        while num_threads > 0:
            print('I am the %s thread' %num_threads)
            threading.Thread(target=thread_message('I am the %s thread' %num_threads)).start()
            time.sleep(0.1)


if __name__ == '__main__':
    unittest.main()
