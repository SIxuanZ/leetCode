#author：张思选
#email：1057950343@qq.com
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        n = len(s)
        c_len = 0
        max_len = 0
        left = 0
        for i in range(n):
            c_len += 1
            while s[i] in a:
                a.remove(s[left])
                left += 1
                c_len -= 1
            if c_len > max_len:max_len = c_len
            a.add(s[i])
        return max_len
