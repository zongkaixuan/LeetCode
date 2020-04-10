#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from learning import randomList


iList = randomList(20)


# 有序数列，二分查找
key = 8
iList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def binarySearch(iList, key):
    iLen = len(iList)
    left = 0
    right = iLen - 1

    while right - left > 1:
        mid = (left + right) // 2
        if iList[mid] < key:
            left = mid
        elif iList[mid] > key:
            right = mid
        else:
            return mid


# 插值查找 -
# 对于等差数列可能是最快的查找方法了
# 但是对于等比数列比二分查找更慢
def insertSearch(iList, key):
    iLen = len(iList)
    left = 0
    right = iLen - 1
    if iList[left] == key:
        return left

    while True:
        mid = left + (key - iList[left]) * (right + left) // \
              (iList[right] - iList[left])
        if mid == left:
            mid += 1

        if key > iList[mid]:
            left = mid
        elif key < iList[mid]:
            right = mid
        else:
            return mid

indexList = [[250, 0], [500,0], [750, 0], [1000, 0]]
def divideBlock():
    global iList, indexList
    sortList = []
    for key in indexList:
        subList = [i for i in iList if i < key[0]]
        key[1] = len(subList)
        sortList += subList
        iList = list(set(iList) - set(subList))

    iList = sortList
    print()
    return indexList


def blockSearch(iList, key, indexList):
    left = 0
    right = 0
    for indexInfo in indexList:
        left += right
        right += indexInfo[1]
        if key < indexInfo[0]:
            break

    for i in range(left, right):
        if iList[i] == key:
            return i

    return -1


if __name__ == "__main__":
    # searcher = binarySearch(iList2, key)
    # searcher = insertSearch(iList2, 5)
    # print(searcher)
    print(iList)
    divideBlock()
    print(iList)
    print(indexList)
