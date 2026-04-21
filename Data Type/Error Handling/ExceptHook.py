import sys
def my_excepthook(exctype, value, traceback):
    print("Something went wrong! Please check your code.")
    #print(exctype)
    #print(value)    
    #print(traceback)
sys.excepthook = my_excepthook
#The upper code will catch any unhandled exceptions and print a custom message instead of the default traceback.
def display():
    print(10+"Hello")
display()