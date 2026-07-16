# 定义函数（使用/和*限制传參方式）
def greet(name, /, gender, age, *, height):
    print(f'我叫{name},性别{gender},今年{age}岁，身高是{height}')


greet('张三', '男', age=18, height=172)

# /和*同时使用时，/必须在*前面
