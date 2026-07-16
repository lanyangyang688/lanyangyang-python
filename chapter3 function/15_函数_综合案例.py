def calc_total(*nums):
    """
    计算总运动量（个）
    :param nums: 每一天的运动量（可变参数）
    :return: 总运动量（个）
    """
    return sum(nums)


def calc_avg(total, days=7):
    """
    计算平均值
    :param total: 总运动量（个）
    :param days: 天数（默认为7）
    :return: 平均值
    """
    return total / days


def check_success(total, goal=120):
    """
    判断本次挑战是否成功
    :param total:总运动量
    :param goal: 成功数量（默认值为120）
    :return: 成功或失败的具体信息
    """
    if total >= goal:
        return '恭喜，挑战成功'
    else:
        return '抱歉挑战失败'


def main(title, duration):
    """
    主函数，用于开始一场挑战赛
    :param title: 比赛标题
    :param duration: 比才持续天数
    :return: none
    """
    print(f'【{title}】【{duration}天】挑战赛（请输入每天的数量）')
    num1 = int(input('第1天：'))
    num2 = int(input('第2天：'))
    num3 = int(input('第3天：'))
    num4 = int(input('第4天：'))
    num5 = int(input('第5天：'))
    num6 = int(input('第6天：'))
    num7 = int(input('第7天：'))
    #计算运动总量
    total = calc_total(num1,num2,num3,num4,num5,num6,num7)
    #计算平均值
    avg = calc_avg(total)
    #判断挑战是否成功
    result = check_success(total)
    #打印相关信息
    print(f'【{title}】【{duration}天】健身总结')
    print('总数：%d,平均值:%.1f'%(total,avg))
    print(result)

main('仰卧起坐',7)


