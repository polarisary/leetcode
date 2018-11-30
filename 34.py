#!/usr/bin/env python
# -*- coding = utf8 -*-

"""
# Created Time: 五 11/16 20:35:22 2018
# File Name   : search_range.py
# Author      : zengwei
# Description :
"""

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = self.binSearch(nums, target)
        # print(idx)
        if idx == -1:
            return [-1, -1]
        left = idx
        right = idx
        while left >= 0 and nums[left] == target:
            left -= 1
                
        while right < len(nums) and  nums[right] == target:
            right += 1
        return [left + 1, right - 1]
            
        
    def binSearch(self, nums, target):
        if (len(nums) == 0) or (nums[0] > target) or (nums[-1] < target):
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            med = int((end - start + 1) / 2) + start
            # print(med)
            if target == nums[med]:
                return med
            elif target < nums[med]:
                end = med - 1
            else:
                start = med + 1
        return -1
        
if __name__ == '__main__':
    print(Solution().searchRange([1,2,3], 3))

# vim: set expandtab ts=4 sts=4 sw=4 :
