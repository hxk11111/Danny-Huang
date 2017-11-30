# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).Find the minimum element.
# You may assume no duplicate exists in the array.

def min_after_rotate_sorted_nums(list):
    low = 0
    high = len(list) - 1
    while low < high:
        mid = (low + high) / 2
        if list[mid] > list[high]:
            # in this case, the min must be in the sublist which starts from mid
            low = mid + 1
        else:
            high = mid
    return low


print  min_after_rotate_sorted_nums([4, 5, 6, 7, 8, 9, 0, 1, 2])
