# 函数嵌套调用测试1
def speak(msg):
    print('-----------')
    print(msg)
    print('-----------')


def greet(name, msg):
    print(f'我叫{name},我想说的话在下面')
    speak(msg)
    print('嗯，我想说的我说完了')


greet('懒羊羊', '你好呀')

print('##########################')


# 函数嵌套调用测试2
def t1():
    print('进入t1函数')
    t2()
    print('退出t1')


def t2():
    print('进入t2函数')
    t3()
    print('退出t2')


def t3():
    print('进入t函数')
    print('正在执行t3函数')
    print('退出t3函数')


t1()
