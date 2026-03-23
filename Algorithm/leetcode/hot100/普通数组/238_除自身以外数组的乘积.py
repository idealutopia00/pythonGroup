from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        
        suf = [1] * n
        for i in range(n-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        
        return [p * s for p, s in zip(pre, suf)]
    
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suf = [1] * n
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        pre = 1
        for i, x in enumerate(nums):
            # 此时 pre 为 nums[0] 到 nums[i-1] 的乘积，直接乘到 suf[i] 中
            suf[i] *= pre
            pre *= x

        return suf

if __name__ == "main":
    pass