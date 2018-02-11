# list去重

orgList = [1, 0, 3, 7, 7, 5]


# 方法一:使用set的特型，python的set和其他语言类似, 是一个无序不重复元素集
def useset(arr):
    return list(set(arr))


# 方法二:使用keys()方法
def usekeys(arr):
    return list({}.fromkeys(arr).keys())


# 方法三: 循环遍历法
def usefor(arr):
    ret = []
    for id in arr:
        if id not in ret:
            ret.append(id)

    return ret


# 方法三: 按照索引再次排序
def userindex(arr):
    formatList = list(set(orgList))
    formatList.sort(key=orgList.index)
    return formatList


if __name__ == '__main__':
    print(useset(orgList))
    print(usekeys(orgList))
    print(usefor(orgList))
    print(userindex(orgList))
