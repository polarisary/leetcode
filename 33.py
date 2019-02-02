#!/usr/bin/env python
# -*- coding = utf8 -*-

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(len(nums) == 0):
        	return -1

        idx = self.get_idx(nums, 0, len(nums)-1)
        print(idx)
        if nums[idx] == target:
        	return idx
        elif nums[idx] < target:
        	return self.bin_search(nums, idx+1, len(nums)-1, target)
        else:
        	return self.bin_search(nums, 0, idx, target)

    def get_idx(self, nums, left, right):
    	if nums[left] < nums[right]:
    		return right
    	med = int(len(nums) / 2)
    	print(med)
    	if nums[med] > nums[right]:
    		# 在右边
    		self.get_idx(nums, med, right)
    	else:
    		if nums[left] < nums[med]:
    			return med
    		self.get_idx(nums, left, med - 1)

    def bin_search(self, nums, left, right, target):
    	med = int((right - left + 1) / 2)
    	if nums[med] == target:
    		return med
    	elif nums[med] < target:
    		return self.bin_search(nums, med+1, right, target)
    	else:
    		return self.bin_search(nums, left, med, target)

if __name__ == '__main__':
	Solution().search([4,5,6,7,0,1,2], 0)

# vim: set expandtab ts=4 sts=4 sw=4 :