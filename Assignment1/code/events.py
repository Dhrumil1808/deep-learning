import threading #library for the thread and events
e = threading.Event() #event is created
thread = [] # array of threads
#function to handle the threads
def main_thread():
    thread_name = threading.current_thread().name
    print 'Thread waiting for event: %s' % thread_name
    e.wait(3) #waits for 3 seconds
    print 'Thread got event: %s' % thread_name
    e.set() #thread is set
    print 'Thread set: %s' % thread_name

for threads in range(4):
    threads = threading.Thread(target=main_thread)
    thread.append(threads)
    threads.start() # creates the thread and calls the "main_thread" function