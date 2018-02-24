import threading, time


# 直接通过初始化thread对象创建
def test():
    t = threading.currentThread()  # 获取当前子线程对象
    print(t.getName())
    i = 0
    while i < 10:
        print(i)
        time.sleep(1)
        i = i + 1


m = threading.Thread(target=test, args=(), name='循环子线程')
m.start()
t = threading.currentThread()
print(t.getName())
