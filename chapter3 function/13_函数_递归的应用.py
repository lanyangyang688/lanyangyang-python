# 使用递归求阶乘
def factorial(num):
    '''使用递归求阶乘'''
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


# 调用函数，求5的阶乘
result = factorial(5)
print(result)
