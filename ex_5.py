"""给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            len1 = expandaroundcenter(s, i, i)
            len2 = expandaroundcenter(s, i, i + 1)
            len_max = max(len1, len2)
            if len_max > (end - start):
                start = i - (len_max - 1) // 2
                end = i + len_max // 2
        return s[start:end + 1]


def expandaroundcenter(s, left, right):
    l, r = left, right
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return r - l - 1