#与日历有关的模块
"""
import calendar

#calendar:获取一年的日历字符串
print(calendar.calendar(2018, l=1, c=5))

#isleap 判断某一年是否是闰年
print(calendar.isleap(2018))

#leapdays 获取指定年份之间的闰年数
print(calendar.leapdays(1996, 2018))

#month获取某个月的日历字符串
print(calendar.month(2018, 11))

#monthrange获取一个月周几开始和天数
print(calendar.monthrange(2018, 11))

#monthcalendar获取一个月每天的矩阵列表
print(calendar.monthcalendar(2018, 11))

#prcal直接打印日历
calendar.prcal(2018)

#时间模块
import time

#time()时间戳,从1979年1月1日0时0分0秒到现在经历的时间
print(time.time())

#timezone当前时区和UTC时间相差的秒数,有夏令时
print(time.timezone)

#altzone,同上,无夏令时
print(time.altzone)

#daylight测试是否是夏令时
print(time.daylight)

#localtime()当前时间
print(time.localtime())

#asctime()返回元组的常字符化后的时间格式
print(time.asctime(time.localtime()))

#ctimeL获取字符串化的当前时间
print(time.ctime())

#mktime使用时间元组获得对应的时间戳
print(time.mktime(time.localtime()))

#clock获取CPU时间 3.0-3.3使用
#sleep使程序进入睡眠,n秒后继续
for i in range(2):
    print("现在是{}秒".format(i))
    time.sleep(1)

#strftime使时间元组转化为自定义的字符串格式
t = time.localtime()
print(time.strftime("%Y年%m月%d日 %H:%M", t))

#datetime模块 提供日期和时间的运算和表示

import datetime
dt = datetime.date(2018, 11, 10)
print(dt)
print(dt.day)
print(dt.year)

#datetime.time提供时间
#datetime.datetime提供时间和日期
#datetime.timedelta 时间变化

t1 = datetime.datetime.now()
print(t1)
td = datetime.timedelta(hours=1)
print(t1+td)

#timeit 时间测量工具
import timeit
c = '''
sum = []
for i in range(1000):
    sum.append(i)
'''
t1 = timeit.timeit(stmt=c, number=100000)
t2 = timeit.timeit(stmt="[i for i in range(1000)]", number=100000)
print(t1)
print(t2)

def doIt():
    num = 3
    for i in range(num):
        print("Repeat for {}".format(i))

t = timeit.timeit(stmt=doIt, number=10)
print(t)

s = '''def doIt(num):
    for i in range(num):
        print("Repeat for {}".format(i))
'''
t = timeit.timeit("doIt(num)", setup=s+"num=3", number=10)
print(t)
"""
#random随机模块 伪随机
import random
#random产生0-1之间的随机数
print(random.random())

#choice 随机返回序列的某个值
l = [str(i)+" hello" for i in range(10)]
print(random.choice(l))

#shuffle()随机打乱列表

l1 = [i for i in range(10)]
print(l1)

random.shuffle(l1)
print(l1)

#randint(a,b) 返回[a,b]的随机整数

for i in range(10):
    print(random.randint(0,2))
