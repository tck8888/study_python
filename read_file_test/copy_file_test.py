import os
import shutil

# 复制文件夹到指定位置

path = r'D:\桌面文件'
newpath = r'D:\yueyue'

allfile = []
filesuffix = ['.doc', '.pdf', '.png', '.jpg', '.rar', '.pptx', '.xlsx']


# 获取所有的文件的地址
def readFile(path):
    allfilelist = os.listdir(path)

    for file in allfilelist:
        filepath = os.path.join(path, file)

        if os.path.isfile(filepath):
            if filepath.endswith(tuple('.doc')) or filepath.endswith(tuple('.pdf')) or filepath.endswith(
                    tuple('.png')) or filepath.endswith(tuple('.jpg')) or filepath.endswith(
                tuple('.rar')) or filepath.endswith(tuple('.pptx')):
                #print(filepath)
                newpaths = filepath.replace(r'D:\桌面文件', newpath)
                # shutil.copyfile(filepath, newpaths)
                print(newpaths)
        else:

            readFile(filepath)


test = []


def copyFile(listFile):
    for file in listFile:
        newname = file.replace(path, newpath)
        # print(newname)
        shutil.copyfile(file, newname)


def copyFile1(listFile):
    for file in listFile:
        file.split()
    return test


if __name__ == '__main__':
    readFile(path)
