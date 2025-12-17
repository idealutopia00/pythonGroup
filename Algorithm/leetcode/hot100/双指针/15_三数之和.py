from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 先排序以便使用双指针
        ans = []
        n = len(nums)
        for i in range(n-2):
            x = nums[i]
            if i > 0 and x == nums[i-1]:
                continue  # 跳过相同起点，避免重复结果
            if x + nums[i+1] + nums[i+2] > 0:
                break  # 当前最小三数之和已大于 0，后面不可能有解
            if x + nums[n-1] + nums[n-2] < 0:
                continue  # 当前最大三数之和仍小于 0，需要继续右移起点
            left = i + 1
            right = n - 1
            while left < right:
                sum = x + nums[left] + nums[right]
                if sum > 0:
                    right -= 1  # 总和偏大，右指针左移
                elif sum < 0:
                    left += 1  # 总和偏小，左指针右移
                else:
                    ans.append([x, nums[left], nums[right]])  # 捕获一组解
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:  # 跳过重复数字
                        left += 1
                    right -= 1
                    while right > left and nums[right] == nums[right + 1]:  # 跳过重复数字
                        right -= 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(solution.threeSum(nums))