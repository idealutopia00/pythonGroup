from typing import List
'''
    给定一个数组 nums,编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
    请注意 ，必须在不复制数组的情况下原地对数组进行操作。
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0  # 记录下一个非零元素要放置的位置
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                print(nums,left)
        
if __name__ == "__main__":
    solution = Solution()
    nums = [0,1,0,0,3,12]
    solution.moveZeroes(nums)