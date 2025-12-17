from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = left = 0
        right = len(height) - 1
        while left < right:
            ans = max(ans, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(solution.maxArea(height))