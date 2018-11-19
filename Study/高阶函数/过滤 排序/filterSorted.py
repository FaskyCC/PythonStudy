#过滤函数filter:对一组数据进行过滤,符合条件的数据生成一个新的列表并返回
def isEven(a):
    return a % 2 ==0
l = [98,0,1,-2,-34,65,-23,49,26,-85,56,223,132,-32,43,-24]
rst=filter(isEven, l)
print(rst)
print([i for i in rst])

#排序sorted 按照给定算法进行排序
sort_l = sorted(l, reverse=False)
print(sort_l)
absSort_l = sorted(l, key=abs, reverse=True)
print(absSort_l)

a = ["danan", "Danan", "Dance", "dance"]
str1 = sorted(a)
print(str1)
str2 = sorted(a, key=str.lower)
print(str2)