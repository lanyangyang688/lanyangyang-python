a = True
b = False
c = 5 > 3
d = 7 < 2
print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)

# 布尔类型是int类型的子类型，底层的本质是用1表示True，用0表示False
print(int(True))
print(int(False))

print(4 + True)
print(8 - False)

print(True + True)
print(True - False)

# 使用bool()将指定内容转换为布尔值，（python中除0以外的任何值转为布尔值后都为True)
print(bool(300))
print(bool(34))
print(bool(-10))
# python中除空字符串以外的任何字符串转为布尔值后都为True
print(bool('hello'))
print(bool('0'))
print(bool('18.5'))
print(bool(''))
