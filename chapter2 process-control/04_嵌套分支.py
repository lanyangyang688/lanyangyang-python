age = int(input('请输入你的年龄:'))
has_report=input('你是是否提交了体检报告？（是/否）')
level=int(input('请输入你的用户等级（1/2/3）'))

if 18 <= age <= 45:
    print('您的年龄符合比赛要求！')
    if has_report == '是':
        print('您已提交体检报告')
        print('您可以参加比赛')
        if level==1:
            print(f'您是{level}级会员，可领取体恤')
        elif level ==2:
            print(f'您是{level}级会员，可领取跑鞋')
        elif level == 3:
            print(f'您是{level}级会员，可领取耳机')
        else:
            print('您输入的等级不正确正确')
    elif has_report == '否':
        print('您未提交体检报告')
    else:
        print('您输入的体检报告有误')
else:
    print('抱歉您的年龄不符合要求')