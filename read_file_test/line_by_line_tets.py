# 逐行读取文件内容

path = r'D:\py_poject_1\study_python\resource\code.txt'

"""
方法一:一行一行的读
优点：节省内存，不需要一次性把文件内容放入内存中
缺点：速度相对较慢
"""


def readFileLineByLine(path):
    f = open(path, encoding='UTF-8', errors='ignore')
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()
    f.close()


"""
方法二:一次读取多行数据
优点：节省内存，不需要一次性把文件内容放入内存中
缺点：速度相对较慢
"""


def readFileLineByLines(path):
    f = open(path, encoding='UTF-8', errors='ignore')
    while 1:
        lines = f.readlines(1000)
        if not lines:
            break
        for line in lines:
            print(line)
    f.close()


"""
方法三：直接for循环
"""


def readFileLineByFor(path):
    for line in open(path, encoding='UTF-8', errors='ignore'):
        print(line)


if __name__ == '__main__':
     readFileLineByLine(path)
    # readFileLineByLines(path)
    # readFileLineByFor(path)
