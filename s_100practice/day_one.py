import math

# 1. 两数求和
def get_sum(num1, num2):
    """求两数和

    :param num1: 数1
    :param num2: 数2
    :return: 和
    """
    return num1 + num2

# 2. 求100以内的偶数并打印
# 偶数：能被2整除的数叫做偶数
def get_even(_max = 100):
    """求一定范围内的偶数

    :param _max: 最大值
    :return: 该范围内的偶数
    """
    i = 0
    while i <= _max:
        if i % 2 == 0:
            print(i)
        i += 1

# 3. 求100以内的奇数并打印
# 奇数：在整数中，不能被2整除的数叫做奇数
def get_odd(_max = 100):
    """求一定范围内的奇数

    :param _max: 最大值，默认为100
    :return: 该范围内的奇数
    """
    i = 0
    while i <= _max:
        if i % 2 == 1:
            print(i)
        i += 1

# 4. 判断素数
# 素数（质数）：在大于1的自然数中，除了1和它本身外，不再有其他因数的自然数
def judge_prime(_i):
    """判断素数

    :param _i: 需要判断的数
    :return: 为素数输出True
    """
    if _i <= 1:
        return False
    i = 2
    while i < _i:
        if _i % i == 0:
            return False
        else:
            i += 1
    return True

# 5. 求阶乘
# 阶乘：正整数的阶乘定义为所有小于及等于该数的正整数的积，记为n!
def get_factorial(_i):
    """求一个数的阶乘

    :param _i: 所求数
    :return: 该数的阶乘
    """
    if _i <= 1:
        return 1
    i = 1
    res = 1
    while i <= _i:
        res = res * i
        i += 1
    return res

# 6. 求圆的周长
def get_circular_girth(_i):
    """求圆的周长

    :param _i: 半径
    :return: 输出3位小数的周长
    """
    _PI = 3.14
    return round(2 * _PI * _i, 3)

# 7. 求圆的面积
def get_circular_area(_i):
    """求圆的面积

    :param _i: 半径
    :return: 面积
    """
    _PI = 3.14
    return round(_PI * _i ** 2, 3)

# 8. 求直角三角形的斜边
def get_right_triangle_hypotenuse(a, b):
    """求直角三角形的斜边

    :param a: 直角边1长
    :param b: 直角边2长
    :return: 斜边长
    """
    return math.sqrt(a * a + b * b)

# 9. 比较三个数的大小并从小到大输出
# 对数组进行排序
def compare_numbers_ez(numbers):
    """对传入列表进行排序

    :param numbers: 一个整数列表
    :return: 直接打印一个排序好的整数列表
    """
    for j in range(len(numbers)):
        for i in range(j + 1, len(numbers)):
            if numbers[i] < numbers[i - 1]:
                numbers[i] = numbers[i - 1] ^ numbers[i]
                numbers[i - 1] = numbers[i] ^ numbers[i - 1]
                numbers[i] = numbers[i - 1] ^ numbers[i]
    for num in numbers:
        print(num, end=" ")

# 0. 找出一个区间内的素数
def find_prime_in(a, b):
    for i in range(a, b):
        if judge_prime(i):
            print(i, end=" ")


if __name__ == '__main__':
    find_prime_in(1, 100)