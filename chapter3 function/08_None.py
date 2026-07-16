# None是一个特殊的字面量，它表示：空值/无值/无意义。
msg = None

# None的类型是NoneType。
print(type(msg))

# None转为布尔值是False。
print(bool(msg))
if not msg:
    print('你好')

# 不能参与数学运算，也不能与字符串拼接。
