name = input('请输入你的名字')
age = input('请输入你的年龄')
#input获取到的内容全都是字符串类型
print(type(age))
print(f'{name},今年的年龄是{age}')
print(f'{name},明年的年龄是{int(age) + 1}')
