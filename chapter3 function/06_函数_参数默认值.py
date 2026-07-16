# 定义函数（设置参数默认值）
def greet(name, gender, age, height, msg='你好'):
    print(f'我叫{name},性别{gender},今年{age}岁，身高是{height}')
    print(f'我想说：{msg}')


# 调用函数
# greet('张三', '男', 18, 172)
# greet('张三', '男', 18, 172,'hello')
greet('张三', '男', 18, 172, msg='hello')


#print函数底层给end函数设置的默认值
print('懒羊羊',end='!!')