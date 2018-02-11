import os

# 检查文件或者文件夹是否存在

path = r'D:\py_poject_1\study_python\resource\code.txt'

if __name__ == '__main__':
    # 既能检测文件，也能检测文件夹是否存在
    if os.path.exists(path):
        print("存在")
    # 既能检测文件，也能检测文件夹是否存在
    if os.path.isfile(path):
         print("是文件")