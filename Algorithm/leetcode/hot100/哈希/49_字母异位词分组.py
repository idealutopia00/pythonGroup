from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word)) # 将单词转换为元组，并排序
            groups[key].append(word)
        return list(groups.values())


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(solution.groupAnagrams([""]))
    print(solution.groupAnagrams(["a"]))
    print(solution.groupAnagrams(["", ""]))
    print(solution.groupAnagrams(["", "b"]))
    print(solution.groupAnagrams(["a", "b"]))
    print(solution.groupAnagrams(["a", "ab"]))
    print(solution.groupAnagrams(["a", "ab"]))
