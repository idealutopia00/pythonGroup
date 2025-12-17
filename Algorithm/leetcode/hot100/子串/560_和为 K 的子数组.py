from collections import defaultdict
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            s[i+1] = s[i] + nums[i]
        
        cnt = defaultdict(int)
        ans = 0
        for i in range(len(nums)+1):
            ans += cnt[s[i] - k]
            cnt[s[i]] += 1
        return ans
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.subarraySum([1, 1, 1], 2))