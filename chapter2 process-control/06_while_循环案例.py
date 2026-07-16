print('需正确回答问题')
riddle = '你是什么人'
answer = '你的心上人'
guess = ''

while guess != answer:
    print(f'问题：{riddle}')
    guess = input('请输入答案')
    if guess == answer:
        print('回答正确')
    else:
        print('回答错误，请再想想')
