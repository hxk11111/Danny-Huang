# encoding=utf-8

# 求对于长度为N的数组A,求子数组的和接 近0的子数组,要求时间复杂度O(NlogN)

def quick_sort(list_pp):
    if len(list_pp) == 1:
        return list_pp[0]
    if len(list_pp) < 1:
        return list_pp
    less = []
    large = []
    target = list_pp[0][1]
    for i in range(1, len(list_pp)):
        if list_pp[i][1] < target:
            less.append(list_pp[i])
        else:
            large.append(list_pp[i])
    return quick_sort(less) + list_pp[0] + quick_sort(large)


def sublist_closest_zero(list_p):
    sum_list = []
    sum_res = 0
    for i in range(len(list_p)):
        sum_res += list_p[i]
        sum_list.append([i, sum_res])
    sorted_sum = quick_sort(sum_list)
    subtract_res = [[(0, 0), abs(sorted_sum[1])]]
    for j in range(2, len(sorted_sum) / 2 + 1):
        index = (sorted_sum[2 * (j - 1)], sorted_sum[2 * (j - 2)])
        res = abs(sorted_sum[2 * j - 1] - sorted_sum[2 * (j - 1) - 1])
        subtract_res.append([index, res])
    return quick_sort(subtract_res)


l = [1, -2, 6, 10, -4, 7, 4, -7 ,-4, 8, 16]
final_res = sublist_closest_zero(l)
final_list = l[min(final_res[0]) + 1:max(final_res[0]) + 1]
sum_res = final_res[1]
print "the sublist which has the sum closest to zero is: ", final_list
print "the sum value is: ", sum_res
# l = [[0, 1], [1, -1], [2, 5], [3, 15], [4, 11], [5, 18], [6, 20], [7, 15]]
# res = quick_sort(l)
# print res

