from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [0] * n
        suf_max = [0] * n
        pre_max[0] = height[0]
        suf_max[n-1] = height[n-1]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], height[i])
        for i in range(n-2, -1, -1):
            suf_max[i] = max(suf_max[i+1], height[i])
        ans = 0
        for i in range(n):
            ans += min(pre_max[i], suf_max[i]) - height[i]
        return ans

if __name__ == "__main__":
    solution = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(solution.trap(height))