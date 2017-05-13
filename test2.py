#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

from pyexcel_xls import get_data
import matplotlib.pyplot as plt

if __name__ == '__main__':
    xlsData = get_data(r"/Users/xixi/Desktop/666.xlsx")
    data = xlsData[u'\u6708\u6da8\u8dcc\u5e45(\u4e0d\u5e26\u516c\u5f0f)']
    code = data[0]
    data = data[1:]
    newData = {}
    for item in data:
        if len(item) == 30:
            newData[item[0]] = item[1:]
    key = sorted(newData)
    first = newData[key[0]][1:]
    first.sort()
    first.reverse()
    dataIndex = []
    for i in range(5):
        dataIndex.append(newData[key[0]].index(first[i]))
    x1 = key
    y1 = []
    for i in key:
        sums = 0
        for j in dataIndex:
            sums += newData[i][j]
        average = sums / 5
        y1.append(average)
    plt.plot(x1, y1, label='跌幅'.decode('utf-8'), linewidth=2, color='b', marker='o',
             markerfacecolor='red', markersize=4)
    plt.xlabel('时间'.decode('utf-8'))
    plt.ylabel('跌幅'.decode('utf-8'))
    plt.title('平均跌幅随时间变化折线图'.decode('utf-8'))
    plt.legend()
    plt.show()
