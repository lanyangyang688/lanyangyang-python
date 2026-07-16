# 使用递归打印n次你好呀（从大到小） 先打印后递归
def welcome(n):
    if n > 1:
        welcome(n - 1)
    print(f'你好呀{n}')


welcome(5)


# 栈结构：先进后出，则可以完成从小到大  先递归后打印
def welcome(n):
    print(f'你好呀{n}')
    if n > 1:
        welcome(n - 1)


welcome(5)
