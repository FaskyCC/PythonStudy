'''
import pkg01.M01

stu = pkg01.M01.Student("菠萝", 18)
stu.selfIntroduce()
pkg01.M01.sayHello()
'''

from pkg01 import *
stu =M01.Student("菠萝", 18)
stu.selfIntroduce()
M01.sayHello()