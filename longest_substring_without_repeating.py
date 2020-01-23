# Brute Force
# Time complexity : O(n^3)
# Space complexity : O(min(n, m))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            tmp = [s[i], ]
            for j in range(i + 1, len(s)):
                if s[j] in tmp:
                    break
                tmp.append(s[j])
            if len(tmp) > max_len:
                max_len = len(tmp)

        return max_len


# Sliding Window
# Time complexity : O(2n) = O(n)
# Space complexity : O(min(m, n))
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        i = 0
        j = 0
        window = []
        while i < len(s) and j < len(s):
            if s[j] not in window:
                window.append(s[j])
                j += 1
                if j - i > max_len:
                    max_len = j - i
            else:
                window.remove(s[i])
                i += 1
        return max_len