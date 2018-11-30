#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Given a string, find the length of the longest substring without repeating
characters.

Example 1:

    Input: "abcabcbb"
    Output: 3 
    Explanation: The answer is "abc", with the length of 3. 
    Example 2:

        Input: "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.
        Example 3:

            Input: "pwwkew"
            Output: 3
            Explanation: The answer is "wke", with the length of 3. 
                         Note that the answer must be a substring, "pwke" is a
                         subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        for i,aim in enumerate(s):
            tmp = s[i+1:]
            for j,v in enumerate(tmp):
                if v not in aim:
                    aim = aim + v
                else:
                    break
            if len(aim) > max:
                max = len(aim)
        return max

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))

# vim: set expandtab ts=4 sts=4 sw=4 :
