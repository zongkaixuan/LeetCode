myList = [7, 3, 5, 1, 9, 4]


def bubble_sort(l):
    if len(l) <= 1:
        return l
    for i in range(1, len(l)):
        for j in range(0, len(l) - i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

    return l


def selection_sort(l: list):
    if len(l) <= 1:
        return l
    for i in range(len(l)):
        if l[i] != min(l[i:]):
            minIdx = l.index(min(l[i:]))
            l[i], l[minIdx] = l[minIdx], l[i]

    return l


def insertion_sort(l: list):
    if len(l) <= 1:
        return l
    for right in range(1, len(l)):
        target = l[right]
        for left in range(0, right):
            if l[right] <= l[left]:
                l[left+1:right+1] = l[left:right]
                l[left] = target
                break

    return l


def merge_sort(l: list):
    if len(l) <= 1:
        return l

    middle = len(l) // 2
    left = l[0: middle]
    right = l[middle:]

    return merge_list(merge_sort(left), merge_sort(right))


def merge_list(left: list, right: list):
    mList = []
    while left and right:
        if left[0] >= right[0]:
            mList.append(right.pop(0))
        else:
            mList.append(left.pop(0))

    while left:
        mList.append(left.pop(0))

    while right:
        mList.append(right.pop(0))

    return mList


def quick_sort(l: list):
    if len(l) <= 1:
        return l
    left = []
    right = []
    for i in l[1:]:
        if i <= l[0]:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [l[0], ] + quick_sort(right)


if __name__ == '__main__':
    # ll = bubble_sort(myList)
    # ll = selection_sort(myList)
    # ll = insertion_sort(myList)
    # ll = merge_sort(myList)
    ll = quick_sort(myList)
    print(ll)
