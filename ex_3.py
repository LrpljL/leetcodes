"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0  # 字符串为空
        n = len(s)
        max_length = 0 #最长子字符串长度
        left = 0       #未重复子字符串左端索引
        curr_length = 0 #窗口检测到当前字符串长度
        s1 = set()      #相当于一个滑动窗口，借助一个集合来存储子字符串
        for i in range(n):
            curr_length += 1 #字符串非空，最长长度至少为1
            while s[i] in s1:   #如果子字符串存在重复，从子字符串的最左端开始删除集合中的元素，直至删除重复元素
                s1.remove(s[left])
                left += 1
                curr_length -= 1
            if curr_length > max_length:
                max_length = curr_length
            s1.add(s[i])
        return max_length