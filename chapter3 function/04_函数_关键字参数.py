# 定义函数（接受位置参数）
def greet(name, gender, age, height):
    print(f'我叫{name},性别{gender},今年{age}岁，身高是{height}')


# 调用函数(关键字参数)
greet(name='张三', gender='男', age=18, height=172)
greet(gender='男', name='张三', height=172, age=18)

# 当关键字参数和位置参数混用时，位置参数必须在关键字参数前面。
