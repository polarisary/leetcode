#!/usr/bin/env python
# -*- coding = utf8 -*-

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            retval = ''
        else:
            retval = s[0]
        i = 1
        while i < (len(s)):
            # print('wwwwww' + str(i))
            tmp = ''
            if (i < len(s)-1) and (s[i-1] == s[i+1]):
                # 返回以i中心最长的回文
                l1 = self.getLongest(i,i,s)
                if len(l1) > len(tmp):
                    tmp = l1
            if s[i-1] == s[i]:
                l2 = self.getLongest(i-1,i,s)
                if len(l2) > len(tmp):
                    tmp = l2
            if len(retval) < len(tmp):
                retval = tmp
            i += 1
        return retval
    
    def getLongest(self, start, end, s):
        while start > 0 and end < len(s)-1:
            # print('ssss:'+str(start)+',end:'+str(end))
            if s[start-1] == s[end+1]:
                start -= 1
                end += 1
            else:
                break
        return s[start:end+1]
            
if __name__ == '__main__':
    print(Solution().longestPalindrome("aaa"))

# vim: set expandtab ts=4 sts=4 sw=4 :
