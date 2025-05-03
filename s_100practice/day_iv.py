# 1. 判断回文数
# 输入一个数字，判断它是不是回文数。
from unittest import case


def is_palindrome(num):
    return str(num) == str(num)[::-1]

# 2. 判断星期几
# 请输入星期几的第一个字母来判断一下是星期几
def what_day():
    w = input('请输入第一个字母:')[0:1]
    match w:
        case 'm':
            print('Monday')
        case 'w':
            print('Wednesday')
        case 'f':
            print('Friday')
        case 's':
            s = input('请输入第二个字母:')[0:1]
            match s:
                case 'a':
                    print('Saturday')
                case 'u':
                    print('Sunday')
        case 't':
            t = input('请输入第二个字母:')[0:1]
            match t:
                case 'h':
                    print('Thursday')
                case 'u':
                    print('Tuesday')

# 3. 相反顺序输出列表
def get_opposite_list(list):
    return list[::-1]

# 4. 对十个数进行排序
def sort_list(list):
    return sorted(list)

# 5. 求一个 3x3 的矩阵对角线之和
def get_matrix_line_sum(matrix):
    return matrix[0][0] + matrix[1][1] + matrix[2][2]

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(get_matrix_line_sum(matrix))