#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should
be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0
    Example 2:

        nums1 = [1, 2]
        nums2 = [3, 4]

        The median is (2 + 3)/2 = 2.5

'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        med = int((len(nums1) + len(nums2) ) / 2)
        merge_list = []
        flag = (len(nums1)+len(nums2)) % 2
        i = j = 0
        while i < len(nums1):
            if j >= (len(nums2)):
                break
            while j < len(nums2):
                if nums1[i] < nums2[j]:
                    merge_list.append(nums1[i])
                    i += 1
                    break
                else:
                    merge_list.append(nums2[j])
                    j += 1
                if len(merge_list) > med:
                    break
        while len(merge_list) <= med:
            if j < len(nums2):
                merge_list.append(nums2[j])
                j += 1
            elif i < len(nums1):
                merge_list.append(nums1[i])
                i += 1
        if flag == 1:
            return merge_list[med]
        else:
            return (merge_list[med-1] + merge_list[med]) / 2

if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1,2],[3,4]))

# vim: set expandtab ts=4 sts=4 sw=4 :
