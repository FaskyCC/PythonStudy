try:
    num = int(input("`请输入数据"))
    result = 100/num
    print("计算结果是 {0}".format(result))
  #  raise SyntaxError
except ValueError as e:
    print("输入有误")
    print(e)
    exit()
except ZeroDivisionError as e:
    print("输入有误")
    print(e)
except Exception:
    print("不知道是什么错误的错误啦")
else:
    print("Very Good")
finally:
    print("程序结束")