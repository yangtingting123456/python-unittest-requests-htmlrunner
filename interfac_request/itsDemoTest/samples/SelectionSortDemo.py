"""
@author:tingting.yang

@time:2020/10/28:17:07

@email:3048903923@qq.com
"""
# 选择排序

def insertion_sort(arr):
    for i in range(1, len(arr)):    # 将 i 看做摸到的牌的下标
        tmp = arr[i]                # 将摸到的牌储存到 tmp
        j = i-1                     # 将 j 看做手里的牌的下标
        while j >= 0 and arr[j] > tmp:  # 如果手里的牌大于摸到的牌
            arr[j+1] = arr[j]       # 将手里的牌往右移一个位置（将手里的牌赋值给下一个位置）
            j -= 1                  # 将手里的牌的下标减 1，再次准备与摸到的牌进行比较
        arr[j+1] = tmp              # 将摸到的牌插入到 j+1 位置
        print(arr)                  # 每一趟比较完了就打印一次


arr = [0, 9, 8, 7, 1, 2, 3, 4, 5, 6]
insertion_sort(arr)