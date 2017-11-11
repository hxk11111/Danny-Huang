# encoding=utf-8

'''
    一、快速排序算法的基本特性
        时间复杂度：O（n*lgn）
        最坏：O（n^2）
        空间复杂度：O（n*lgn）
        不稳定。
        快速排序是一种排序算法，对包含n个数的输入数组，平均时间为O（nlgn），最坏情况是O（n^2）。
        通常是用于排序的最佳选择。因为，基于比较的排序，最快也只能达到O（nlgn）。

    二、快速排序算法的描述
        1.分解：
            A[p..r]被划分为俩个（可能空）的子数组A[p ..q-1]和A[q+1 ..r]，使得
            A[p ..q-1] <= A[q] <= A[q+1 ..r]
        2.解决：通过递归调用快速排序，对子数组A[p ..q-1]和A[q+1 ..r]排序。
        3.合并。
'''


def partition(l, low, high):
    i = low
    refer = l[low]
    for j in range(low + 1, high + 1):
        if l[j] <= refer:
            i += 1
            l[i], l[j] = l[j], l[i]
    l[low], l[i] = l[i], l[low]
    return i


def quick_sort(data, low, high):
    if low < high:
        k = partition(data, low, high)
        quick_sort(data, low, k - 1)
        quick_sort(data, k + 1, high)


list_data = [5, 2, 6, 3, 9, 11, 4, 8]
quick_sort(list_data, 0, len(list_data) - 1)
print list_data
