from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortNums = sorted(list(set(nums)))
        maxLength = 0
        currentLength = 0
        for i in range(len(sortNums)):
            if i == 0 or sortNums[i] == sortNums[i-1] + 1:
                currentLength += 1
            else:
                maxLength = max(maxLength, currentLength)
                currentLength = 1
        maxLength = max(maxLength, currentLength)
        return maxLength

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))