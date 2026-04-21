import threading
import time

def custom_threading_excepthook(args):
    print("\033[95mAn exception occurred in a thread!\033[0m")
    print('\033[91mClass:\033[0m', args[0])
    print('\033[91mValue:\033[0m', args[1])
    print('\033[91mTraceback:\033[0m', args[2])
    print('\033[91mThread:\033[0m', args[3])

def display():
    for i in range(5):
        print(100 + 'Hello,World')
        time.sleep(1)
def show():
    for i in range(5):
        print('\033[92mWelcome to Python\033[0m')
        time.sleep(1)
threading.excepthook = custom_threading_excepthook
# Create a thread to run the display function
thread1 = threading.Thread(target=display)
thread2 = threading.Thread(target=show)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("\033[94mAll threads have finished execution.\033[0m")

