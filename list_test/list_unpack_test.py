# 解包用法

# 将list中每个元素赋值给一个变量
name, age, date = ['Tck', 28, '2018-02-24']
print(name)

# 可迭代对象都可以这样做
# 列表
a, b, c = ['a', 'b', 'c']
print(a)
a, b, c = enumerate(['a', 'b', 'c'])
print(a)
# 元组
a, b, c = ('a', 'b', 'c')
print(a)
# 字典
a, b, c = {'a': 1, 'b': 2, 'c': 3}
print(a)
a, b, c = {'a': 1, 'b': 2, 'c': 3}.items()
print(a)
# 字符串
a, b, c = 'abc'
print(a)
# 生成器
a, b, c = [x + 1 for x in range(3)]
print('a=%d,b=%d,c=%d' % (a, b, c))

# 如果可迭代对象包含的元素和前面待赋值变量数量不一致，则会报错。但是可以通过*来表示多个元素
first, *new, last = [94, 85, 73, 46]
print(new)
# 压包是解包的逆过程，用zip函数实现
a = ['a', 'b', 'c']
b = [1, 2, 3]
for i in zip(a, b):
    print(i)

a = [1, 2, 3]
b = [1, 2, 3]
for i, j in zip(a, b):
    print(i + j)

l = [('Bob', '1990-1-1', 60),
     ('Mary', '1996-1-4', 50),
     ('Nancy', '1993-3-1', 55)]
for name, *args in l:
    print(name, args)

# 当一些元素不用时，用_表示是更好的写法，可以让读代码的人知道这个元素是不要的
person = ('Bob', 20, 50, (11, 20, 2000))
name, *_, (*_, year) = person
print(name)
print(year)


# *之可变参数
def myfun(*num):
    print(num)


myfun(1, 2)


# *之关键字参数
def myfun(**kw):
    print(kw)


myfun(name="Tck", age=20)


# (1)函数传入实参时，可变参数(*)之前的参数不能指定参数名
def myfun(a, *b):
    print(a)
    print(b)


myfun(10, 6, 3)


# (2)函数传入实参时，可变参数(*)之后的参数必须指定参数名，否则就会被归到可变参数之中
def myfun(a, *b, c=None):
    print(a)
    print(b)
    print(c)


myfun(1, 2, 3, c=66)


# (3)关键字参数都只能作为最后一个参数，前面的参数按照位置赋值还是名称赋值都可以
def myfun(a, *b, c, **d):
    print(a)
    print(b)
    print(c)
    print(d)


myfun(1, 2, 3, c=4, m=5, n=6)


# (4)可变参数与关键词参数共同使用以表示任意参数
def mydecorator(func):
    def wrapper(*args, **kw):
        print('I am using a decorator.')
        return func(*args, **kw)

    return wrapper


@mydecorator
def myfun(a, b):
    print(a)
    print(b)


myfun(1, b=2)
