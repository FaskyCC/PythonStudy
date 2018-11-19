stm = lambda x, y, z: x+10*y+100*z
print(stm (1,2,3))

def funcA(n):
    return n*100

def funcB(n):
    return funcA(n)*3

def funcC(n, f):
    return f(n)*3
print(funcB(100))
print(funcC(100,funcA))

#map函数每个元素按照一定的规则进行操作,返回值是迭代对象
l1 = [i for i in range(10)]
def multen(n):
    return n*10
l2 = map(multen, l1)
for i in l2:
    print(i)

#reduce函数把一个迭代对象最后归并为一个结果,对函数参数有要求,必须要两个参数,必须返回结果

from functools import reduce
def myAdd(x, y):
    return x+y

print("*"*20)
print(reduce(myAdd, [1,2,3,4,5]))

