#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Given an array of integers, return indices of the two numbers such that they add
up to a specific target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, v in enumerate(nums):
            t = nums[i+1:]
            for j,val in enumerate(t):
                if (v + val) == target :
                    return (i,i+1+j)

if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([3, 2, 4], 6))


# vim: set expandtab ts=4 sts=4 sw=4 :
