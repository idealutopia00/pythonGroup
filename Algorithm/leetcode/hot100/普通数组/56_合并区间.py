from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        for interval in intervals:
            # ans 初始为空，需要一个控制初始化的条件
            if not ans or ans[-1][1] < interval[0]: 
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))