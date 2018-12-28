#守护线程,即为随主进程结束而结束的线程,主进程结束即为程序结束

import time
import threading

def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")

print("Main thread")

t1 = threading.Thread(target=fun, args=())
# 设置守护线程的方法，必须在start之前设置，否则无效
t1.setDaemon(True)
#此处设为False,程序会在主进程和t1进程都结束才会退出
#t1.daemon = True
t1.start()
time.sleep(1)
print("Main thread end")
