'''
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

输入：
s = "abcd"
t = "abcde"

输出：
e
'''
s = "abcd"
t = "abcde"
for i in s:
    t = t.replace(i, '', 1)
print(t)