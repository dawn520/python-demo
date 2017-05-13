#!/usr/local/bin/python
# -*- coding: UTF-8 -*-


# 126, 324, 119, 13, 418
originList = [126, 253, 418, 4, 65, 741, 119, 324, 25, 976, 540, 13, 482, 659, 88, 932]
originList.sort()
aList = []
result = []
for i in range(0, 16, 4):
    aList.append(originList[i:i + 4])
print aList
for j in range(3):
    for k in range(j + 1, 4):
        item = aList[j]
        item1 = aList[k]
        sums = item[0] + item[1] + item[2] + item[3]
        sums1 = item1[0] + item1[1]
        sums2 = item1[2] + item1[3]
        if sums + sums1 == 1000:
            result = item + item1[0] + item1[1]
            break
        elif sums + sums2 == 1000:
            result = item + item1[2] + item1[3]
            break
        elif sums + sums1 < 1000 and sums + sums2 > 1000:
            for a in range(2):
                for b in range(2, 4):
                    sums3 = item1[a] + item1[b]
                    if sums + sums3 == 1000:
                        result = item + item1[a] + item1[b]
                        break
print result
