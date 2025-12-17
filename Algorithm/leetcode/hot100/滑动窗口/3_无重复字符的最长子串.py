from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        for right in range(len(s)):
            cnt[s[right]] += 1
            while cnt[s[right]] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

if __name__ == "__main__":
    s = "abcabcbb"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))