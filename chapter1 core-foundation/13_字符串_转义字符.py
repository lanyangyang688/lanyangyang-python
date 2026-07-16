# 使用\'输出'
from dask.array.dispatch import to_cupy_dispatch

print('python中,可以使用\'包裹一个字符串')

# 使用\"输出"
print('python中,可以使用\"包裹一个字符串')

# 使用\n进行换行
print('注册会员需要以下信息：\n姓名\n年龄\n手机号')

#使用\\输出\
print('D:\\nice')

print('***********************')
#使用\b删除前一个字符
print('helloo\b')

#使用\r使光标回到本行开头，覆盖输出
print('67%\r68%')

#使用\t表示水平制表符（让光标跳转到下一位制表位）
print('1234123412341234')
print('ab\tcd')
print('abc\td')
print('abcd\ta')
print('我是\t中文')