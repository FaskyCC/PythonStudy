#返回函数,函数返回可以是一个值也可以是函数
def myF(a):
    print("In myF")
    return None
def myF2():
    def myF3():
        print("In myF3")
        return 3
    return myF3
f3 = myF2()
f3()

#复杂的返回函数
def myF4(*args):
    def myF5():
        rst = 0
        for n in args:
            rst +=n
        print(rst)
        return rst
    return myF5
f5 = myF4(1,2,3,4,5)
f5()

#返回函数不能引用循环变量,注意version1和version2的区别
#version1
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

#version2
def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count1()
print(f1())
print(f2())
print(f3())

#装饰器:在不改动函数代码的基础上无限扩展功能,返回函数的高阶函数
import time
def hello():
    print("Hello World")
f = hello
f()

#定义装饰器,在打印之前打印系统时间
def printTime(f):
    def wrapper (*args, **keyargs):
        print("Time:", time.ctime())
        return f(*args, **keyargs)
    return wrapper
#使用时使用@
@printTime
def hello():
    print("Hello World")
hello()

#偏函数,有特定参数的函数体functools.partial的作用是把某些函数固定返回一个新的函数
import functools
int16 = functools.partial(int, base = 16)
print(int16("12345"))