# 定义函数（使用*args去接收：可变位置参数）
def test1(*args):
    # 此处args的值，是一种新的数据类型，叫元组。
    print(args)


# 调用函数
test1('张三', '男', 18, 172)


# 定义函数（使用**kwargs去接收：可变关键字参数）
def test2(**kwargs):
    # 此处**kwargs的值，是一种新的数据类型，叫字典。
    print(kwargs)


# 调用函数
test2(name='张三', gender='男', age=18, height=172)


# 定义函数（同时使用：可变位置参数，可变关键字参数）
def fun3(a, b, *args, **kwargs):
    print('@@@@@@@@')
    print(a)
    print(b)
    print(args)
    print(kwargs)


# 调用函数
fun3('张三', '男', '抽烟', '喝酒', age=18, height=172)
