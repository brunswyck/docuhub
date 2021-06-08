*********
threading
*********

non-blocking
============

first example
-------------

.. code-block:: python

   from threading import Thread
   import time
   
   
   class ThreadFunction(Thread):
       def __init__(self, name):
           Thread.__init__(self)
           self.name = name
   
       def run(self):
           print(f"Thread {self.name}: starting")
           time.sleep(2)
           print(f"Thread {self.name}: finishing")
   
   
   if __name__ == '__main__':
       for i in range(5):
           thread = ThreadFunction(i)
           thread.start()
   """
   Thread 0: starting
   Thread 1: starting
   Thread 2: starting
   Thread 3: starting
   Thread 4: starting
   Thread 2: finishingThread 0: finishingThread 1: finishing
   
   
   Thread 3: finishing
   Thread 4: finishing
   """

each iteration runs in parallel and is executed at the same time. So the final script will only last 2 seconds in total since the code is not blocking.

Parallel programming can be very convenient, but it also has its pitfalls. We will now look at some of them and the methods that exist to avoid them.

thread synchronization
======================

Programming multiple instruction streams brings its share of difficulties. At first glance, it seems very convenient to have several parts of our code running at the same time. During a task that may take a long time to run (perhaps downloading information from a website) we can do something else, not just wait for the resource to be downloaded.

But development can be proportionately more complicated. You have to keep in mind that different instruction streams can be advanced to different points at a given time.

example
-------

.. code-block:: python

   class MyThread(Thread):
       def __init__(self, text):
           Thread.__init__(self)
           self.text = text
       
       def run(self):
           print(self.text)
           with open('threads.txt', 'a') as f:
               f.write(self.text)
   
   thread_1 = MyThread("My First thread! ")
   thread_2 = MyThread("My Second thread! ")
   thread_3 = MyThread("My third thread! ")
   thread_4 = MyThread("My fourth thread! ")
   
   thread_1.start()
   thread_2.start()
   thread_3.start()
   thread_4.start()
   
   f = open("threads.txt")
   f.read()
   # My Second thread! My First thread! My third thread! My 4e thread!


lock
----


There are several ways to "synchronize" our threads, i.e. to make some of the code only run if no one is using the shared resource. The simplest synchronization mechanism is the lock.

It is an object proposed by `threading` that is extremely simple to use: at the beginning of our instructions that use our shared resource, we tell the lock to block for the other threads. If another thread wants to use this resource, it must wait until it is released.

.. code-block:: python

   from threading import Thread, RLock

   lock = RLock()

   class SyncThread(Thread):
       def __init__(self, text):
           Thread.__init__(self)
           self.text = text

       def run(self):
           with lock:
               print(self.text)
               with open('synch_thread.txt', 'a') as file:
                   file.write(self.text)

   thread_1 = SyncThread("Thread 1 /")
   thread_2 = SyncThread("Thread 2 /")
   thread_3 = SyncThread("Thread 3 /")
   thread_4 = SyncThread("Thread 4 /")

   thread_1.start()
   thread_2.start()
   thread_3.start()
   thread_4.start()


- We import `RLock` from the threading module
- We create a lock that we put into our `lock` variable
- In our `run` method, we lock part of our thread.

.. code-block:: python

   from threading import Thread, RLock
   
   lock = RLock()
   
   
   class SyncThread(Thread):
       def __init__(self, text):
           Thread.__init__(self)
           self.text = text
   
       def run(self):
           with lock:
               print(self.text)
               with open('sync_thread.txt', 'a') as file:
                   file.write(self.text)
   
   
   if __name__ == '__main__':
       thread_1 = SyncThread("Thread 1 /")
       thread_2 = SyncThread("Thread 2 /")
       thread_3 = SyncThread("Thread 3 /")
       thread_4 = SyncThread("Thread 4 /")
   
       thread_1.start()
       thread_2.start()
       thread_3.start()
       thread_4.start()
       f = open("sync_thread.txt")
       f.read()
       # thread order will always be the same
       # Thread 1 /
       # Thread 2 /
       # Thread 3 /
       # Thread 4 /
