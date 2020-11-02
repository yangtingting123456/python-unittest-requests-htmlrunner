"""
@author:tingting.yang
@time:2020/10/29:11:12
@email:3048903923@qq.com
"""

# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2


class Solution(object):
    def twoSum(self, numbers, target):
        l=0
        r=len(numbers)-1
        while(l<r):
            if(numbers[l]+numbers[r]== target):
                return [l+1,r+1]
            if(numbers[l]+numbers[r] <target):
                l += 1
            else:
                r -= 1


