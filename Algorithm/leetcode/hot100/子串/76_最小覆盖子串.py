from collections import Counter
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_s = Counter()
        cnt_t = Counter(t)
        
        ans_left, ans_right = -1, len(s)
        left = 0
        for right, c in enumerate(s):
            cnt_s[c] += 1
            while cnt_s >= cnt_t:
                if right - left< ans_right - ans_left:
                    ans_left, ans_right = left, right
                cnt_s[s[left]] -= 1
                left += 1
        return s[ans_left:ans_right+1] if ans_left != -1 else ""

class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        cnt = defaultdict(int)  # 比 Counter 更快
        for c in t:
            cnt[c] += 1
        less = len(cnt)  # 有 less 种字母的出现次数 < t 中的字母出现次数

        ans_left, ans_right = -1, len(s)
        left = 0
        for right, c in enumerate(s):  # 移动子串右端点
            cnt[c] -= 1  # 右端点字母移入子串
            if cnt[c] == 0:
                # 原来窗口内 c 的出现次数比 t 的少，现在一样多
                less -= 1
            while less == 0:  # 涵盖：所有字母的出现次数都是 >=
                if right - left < ans_right - ans_left:  # 找到更短的子串
                    ans_left, ans_right = left, right  # 记录此时的左右端点
                x = s[left]  # 左端点字母
                if cnt[x] == 0:
                    # x 移出窗口之前，检查出现次数，
                    # 如果窗口内 x 的出现次数和 t 一样，
                    # 那么 x 移出窗口后，窗口内 x 的出现次数比 t 的少
                    less += 1
                cnt[x] += 1  # 左端点字母移出子串
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.minWindow("ADOBECODEBANC", "ABC"))

# 覆盖