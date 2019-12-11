import threading
import time
import io

class MyThread(threading.Thread): #create the thread
    def run(self):
        print("{} started!".format(self.getName()))              # "Thread-x started!"
        with io.open("C:\\Users\\Callum\\code\\text_" + str(x) + ".txt", 'w', encoding='utf-8') as f:  # Thread Workload
            f.write(unicode("Hello World"))                                                            # Thread Workload
            f.write(unicode(x))                                                                        # Thread Workload
        print("{} finished!".format(self.getName()))             # "Thread-x finished!"

for x in range(4):                                     #How Many times
    mythread = MyThread(name = "Thread-{}".format(x + 1))  #Create Thread & assign ID
    mythread.start()                                   #Start the thread, invoke the run method
    time.sleep(.9)#Wait 0.9 seconds before starting another
    x=x+1 #loop counter