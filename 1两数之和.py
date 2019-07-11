#1.两数之和
# 遍历
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic=dict()
        for index,value in enumerate (nums):
            sub = target - value
            if sub in dic:
                return [dic[sub], index]
            else:
                dic[value] = index
