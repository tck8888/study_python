import threading
import time


# 通过基础thread类来创建
# 继承Thread
class MyThread(threading.Thread):
    def __init__(self, name):
        super(MyThread, self).__init__(name=name)
        print('线程名' + name)

    def run(self):
        i = 0
        while i < 10:
            print(i)
            time.sleep(1)
            i = i + 1


if __name__ == '__main__':
    t = MyThread('mythread')
    t.start()
