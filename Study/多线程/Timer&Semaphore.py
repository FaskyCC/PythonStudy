import threading
import time

# 参数定义最多几个线程同时使用资源
semaphore = threading.Semaphore(3)

def func():
    if semaphore.acquire():
        print(threading.currentThread().getName() + ' get semaphore')
        time.sleep(8)
        semaphore.release()
        print(threading.currentThread().getName() + ' release semaphore')

def func2():
    for i in range(8):
        t1 = threading.Thread(target=func)
        t1.start()

if __name__ == "__main__":
    t = threading.Timer(6, func2)
    t.start()

    i = 0
    while True:
        print("{0}***************".format(i))
        time.sleep(3)
        i += 1