

from typing import List


def twoSum( nums: List[int], target: int) -> List[int]:
    for i,num in enumerate(nums):
        num2 = target-num
        if num2 in nums:
            return i,nums.index(num2)

print(twoSum([1,2,3,4],3))

a=[1,2,3,4]
print(a[:])

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            num2 = target-num
            if num2 in nums[i+1:] :
                return i,i+1+nums[i+1:].index(num2)