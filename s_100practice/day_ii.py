from day_i import judge_prime


# 1. 组合数字：有四个数字，1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少
def get_no_repeat_nums():
    digit = [1, 2, 3, 4]
    three_digit_nums = []
    for i in digit:
        for j in digit:
            for k in digit:
                if i != j and i != k and j != k:
                    three_digit_nums.append(i * 100 + j * 10 + k)
    print(f'共有{len(three_digit_nums)}个不相同的数字' + '分别是：')
    print(three_digit_nums)

# 2. 打印乘法口诀表
def get_multiplication_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f'{i} * {j} = {i * j}', end='\t')
        print('\n')

# 3. 水仙花数
# 水仙花数：是一个三位数，各位数字立方和等于该数字本身
def get_daffodil_num():
    for i in range(1, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                num = i * 100 + j * 10 + k
                if num == i ** 3 + j ** 3 + k ** 3:
                    print(num, end=' ')

# 4. 反向输出四位数：输入一个四位数，反向输出对应的四位数
def reverse_num(num):
    i = num % 1000 # 321
    j = num % 100 # 21
    k = num % 10 # 1
    m = (num - i) / 1000 # 4
    i = (i - j) / 100 # 3
    j = (j - k) / 10 # 2
    return int(k * 1000 + j * 100 + i * 10 + m)

# 5. 字母判断：输入一个字符，判断是否为字母
def is_letter(letter):
    i = ord(letter)
    if (65 <= i <= 90) or (97 <= i <= 122):
        return True
    else:
        return False

# 6. 判断三角形
def is_triangle(triangle):
    if len(triangle) != 3:
        print("error!")
        return False
    for i in triangle:
        if i <= 0:
            return False
    a, b, c = sorted(triangle)
    return a + b > c

# 7. 求完数
# 完数：一个数恰好等于除了它以外的因子之和
def get_prefect_num(max):
    result = set()
    for i in range(1, max + 1):
        k = []
        for j in range(1, i + 1):
            if (i % j == 0) and (j != i):
                k.append(j)
        if sum(k) == i:
            result.add(i)
    print(sorted(result))
    return None

# 8. 求质数因子
def get_prime_factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            if judge_prime(i):
                print(i, end=' ')

# 9. 海伦公式求三角形面积
def get_triangle_area(triangle):
    if is_triangle(triangle):
        p = (sum(triangle) / 2)
        x = 1
        for i in triangle:
            x = x * (p - i)
        s = (p * x) ** 0.5
        return s
    else:
        return False

# 0. 判断某年某天
class WhatDay:
    def __init__(self):
        self.year = int(input("year:"))
        self.mon = int(input("mon:"))
        self.day = int(input("day:"))
        self.leap = self.is_leap_year()

    def is_leap_year(self):
        """判断是否为闰年"""
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)

    def day_of_year(self):
        """计算该年的第几天"""
        # 每个月的天数（非闰年）
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # 如果是闰年，二月有29天
        if self.leap:
            days_in_month[1] = 29

        # 计算该年的第几天
        day_count = self.day
        for i in range(self.mon - 1):
            day_count += days_in_month[i]

        return day_count


if __name__ == '__main__':
    Day = WhatDay()
    print(Day.day_of_year())