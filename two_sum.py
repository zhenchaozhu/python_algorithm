# coding: utf-8

"""
给一个int型数组，要求找出其中两个和为特定值的数的坐标。
注意点：
返回的坐标一要比坐标二小
最小的坐标是1，不是0
例子：
输入: numbers={2, 7, 11, 15}, target=9 输出: index1=1, index2=2
解题思路

第一遍遍历整个数组，用map记录数值和它的坐标，第二遍遍历数组，判断（目标数字-当前数字）是否在map中，如果在，且它的下标与当前数字的下标不相同，
则说明存在这两个数，返回坐标。
"""

class Solution(object):

    def two_sum(self, nums, target):

        hash_map = {}
        for index, value in enumerate(nums):
            hash_map[value] = index

        for index1, value in enumerate(nums):
            if (target - value) in hash_map:
                index2 = hash_map[target - value]
                if index1 < index2:
                    return [index1 + 1, index2 + 1]


if __name__ == '__main__':
    solution = Solution()
    solution.two_sum([1,3,5,11], 8)
