#打印菱形

def draw(num):
    a="*"*(2*(c-num)+1)
    print(a.center(b,' '))
    if num!=1:
        draw(num-1)
        print(a.center(b,' '))
for num in range(1,5):
    num = int(num)
    c = num
    b = 11
    draw(num)

import os
print(os.name)