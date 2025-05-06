"""
Python 操作 Excel 自动化
实现功能：
    1. 读入Excel数据
    2. 实现快捷查询
步骤：
    1. 读取（使用Pandas）
    2. 分析（使用Pandas输出）
"""
import pandas as pd


if __name__ == '__main__':
    io = r'excel/douban_top250.xlsx'
    oo = r'excel/after.xlsx'
    data = pd.read_excel(io, sheet_name= 0)
    # data['year'] = data['pubdate'].apply(lambda x: x.split('-')[0])
    # data['month'] = data['pubdate'].apply(lambda x: x.split('-')[1])
    # data['day'] = data['pubdate'].apply(lambda x: x.split('-')[2])
    writer = pd.ExcelWriter(oo)
    # data.to_excel(writer, sheet_name= '原始数据')
    # writer.close()
    # for i in data['year'].unique():
    #     data[data['year'] == i].to_excel(writer, sheet_name=i)
    genre = set(z for i in data['genre'] for z in i.split(','))
    for ty in genre:
        data[data['genre'].str.contains(ty)].to_excel(writer, sheet_name=ty)

    writer.close()

