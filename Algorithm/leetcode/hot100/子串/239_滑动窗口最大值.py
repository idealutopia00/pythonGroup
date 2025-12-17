from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * (len(nums) - k + 1)
        q = deque()
        for i, x in enumerate(nums):
            # print(q)
            # print(ans)
            while q and nums[q[-1]] < x:
                q.pop()
            q.append(i)
            left = i - k + 1
            if q[0] < left:
                q.popleft()
            if left >= 0:
                ans[left] = nums[q[0]]
        return ans
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))