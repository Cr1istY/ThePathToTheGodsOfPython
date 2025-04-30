import time
from day_i import get_factorial


# 1. 斐波那契数列，找出第 n 个项
def get_fibonacci(n):
    res = 0
    if n <= 3:
        return 1
    res = get_fibonacci(n-1) + get_fibonacci(n-2)
    return res

# 2. 将一个列表的数据复制到另一个列表
def copy_list(list):
    return [i for i in list]

# 3. 暂停一段时间后输出
def pause_print(target):
    time.sleep(1)
    print(target)

# 4. 利用条件运算符的嵌套完成：成绩大于90的为A，成绩大于70的为B，小于60为D
def is_good(list):
    grace = []
    for grade in list:
        if grade >= 90:
            grace.append('A')
        elif grade >= 70:
            grace.append('B')
        elif grade >= 60:
            grace.append('C')
        else:
            grace.append('D')
    return grace

# 5. 输入一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数
def is_character(list):
    target = {'character': 0, 'blank': 0, 'number': 0, 'other': 0}
    for i in list:
        i = ord(i)
        if i == 32:
            target['blank'] += 1
        elif 49 <= i <= 57:
            target['number'] += 1
        elif 65 <= i <= 90:
            target['character'] += 1
        elif 97 <= i <= 122:
            target['character'] += 1
        else:
            target['other'] += 1
    print(target)

# 6. 落体反弹问题：一球从100米高度自由落下，每次落地后跳回原有高度的一半；
# 再落下时，求它在第十次落地时，共经过多少米？第十次反弹多高？
def ball_fall(height):
    count = 0
    while count < 10:
        if count == 0:
            sum = height
        else:
            sum += (height * 2)
        height /= 2
        count += 1
    print(sum, height)

# 7. 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾又偷吃了一个。
# 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。
# 到第十天早上想再吃时，见只剩下一个桃子，求第一天共摘了多少个桃子。
def monkey_peach():
    day = 10
    peach = 1
    day_peach = []
    while day >= 1:
        day_peach.append(peach)
        peach = (peach + 1) * 2
        day -= 1
    print(day_peach)

# 8. 求指定数列的和
# 有一分数列：2/1、3/2、5/3、8/5、13/8 求出这个数列前20项的和
def get_list_sum():
    a = 2
    b = 1
    list = []
    for i in range(20):
        list.append(a / b)
        temp = b
        b = a
        a = temp + a
    print(sum(list))

# 9. 求各个阶乘的和
def get_facto_sum(max):
    list = [get_factorial(i) for i in range(1, max + 1)]
    print(sum(list))

# 0. 年龄急转弯
# 有5个人坐在一起，问第五个人多少岁？
# 他说比第四个人大2岁，第四个人说比第三个人大两岁
# 最后一个人10岁，问第五个人多少岁
def get_age():
    age = 10
    for i in range(4):
        age += 2

    print(age)

if __name__ == '__main__':
    get_age()