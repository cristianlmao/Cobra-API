import webbrowser
import time


#console
class console:
    def write(msg):
        print(msg)
        
    def prefix_write(prefix, msg):
        print("[" + prefix + "] " + msg)

#Debug   
class debug:
    def prefix_error(prefix, msg):
        print("\u001b[31m" + "[" + prefix + "] " + msg + "\u001b[0m")
        
    def error(msg):
        print("\u001b[31m" + msg + "\u001b[0m")
        
    def prefix_warning(prefix, msg):
        print("\u001b[33m" + "[" + prefix + "] " + msg + "\u001b[0m")
        
    def warning(msg):
        print("\u001b[33m" + msg + "\u001b[0m")

#Cobra
class cobra:
    def version():
        print("WRITE 'cobra.test()' IN YOUR PROJECT TO TEST IF ITS IMPORTED SUCCESFULY! | Version: 1")
        
    def test():
        debug.prefix_error("TEST", "THIS IS JUST A TEST!!!")
        debug.prefix_warning("TEST", "THIS IS JUST A TEST!!!")
        debug.error("THIS IS JUST A TEST!!!")
        debug.warning("THIS IS JUST A TEST!!!")
        
#single commands

def openurl(url):
    webbrowser.open(url)
    
def stop():
    time.sleep(86400 * 7)
     
def delay(seconds):
    time.sleep(seconds)