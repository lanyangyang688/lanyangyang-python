#使用==来判断左右两侧是否相等（需为同一类型）
a = 5
b = 7
c='5'
result = a == c
print(result)

#使用!=判断左右两边是否不等
a = 5
b = 7
result = a != b
print(result)

msg1='abc'
msg2='xyz'
msg3='我爱你'
msg4='中国'
msg5='abc'
msg6='abcef'
print(msg5>msg6)

#通过ord()查看指定字符的unicode编码
print(ord('a'))
print(ord('我'))

#使用chr()将unicode编码转为字符
print(chr(97))
print(chr(25105))