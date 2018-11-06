#创建一个类
class PythonStudent():
    name = None
    age = 18
    course = "python"
    def doHomework(self):
        print("我在做作业呢")
        return None
stu = PythonStudent()
stu.name = "菠萝"
print(stu.name)
print(stu.age)
print(stu.course)
stu.doHomework()
