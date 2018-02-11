# 两个list的差集、交集与并集的方法

# list的差集
listA = [1, 2, 3, 4]
listB = [2, 3, 4]


# 方法一: 循环遍历
def differenceSetList_for(arr1, arr2):
    ret = []
    for i in arr1:
        if i not in arr2:
            ret.append(i)
    return ret


# 方法二: 运算符
def differenceSetList_operator(arr1, arr2):
    return list(set(arr1) ^ set(arr2))


# 方法三: difference函数法
def differenceSetList_difference(arr1, arr2):
    return list(set(arr1).difference(set(arr2)))


print(differenceSetList_for(listA, listB))
print(differenceSetList_operator(listA, listB))
print(differenceSetList_difference(listA, listB))

print("--------------------")


# list的并集

def list_union_list(arr1, arr2):
    return list(set(arr1).union(set(arr2)))


print(list_union_list(listA, listB))


# 两个list的交集

def list_intersection_list(arr1, arr2):
    return list(set(arr1).intersection(set(listB)))


print("--------------------")

print(list_intersection_list(listA, listB))
