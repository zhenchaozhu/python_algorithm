# coding: utf-8

class Solution(object):

    def solution(self, s):
        exists = {}
        s_len = 0
        left = 0
        for i in range(len(s)):
            if s[i] in exists and exists[s[i]] >= left:
                 left = exists[s[i]] + 1

            exists[s[i]] = i
            s_len = max(s_len, i - left + 1)

        return s_len