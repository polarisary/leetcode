#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    # 其实，可以重写比较运算符，直接调用sorted函数排序，但LeetCode不允许重写Interval类，子类也不行，所以这里必须要自己写排序，快排可以满足实际要求
    def __lt__(self, other):
        return self.start < other.start
    
    def __eq__(self, other):
        return self.start == other.start

    def __repr__(self):
        return 'Interval({},{})'.format(self.start, self.end)

class Solution(object):
    # 快速排序
    def quick_sort(self, array, left, right):
        if left >= right:
            return
        low = left
        high = right
        key = array[low]
        while left < right:
            while left < right and array[right].start > key.start:
                right -= 1
            array[left] = array[right]
            # print('right',array)
            while left < right and array[left].start <= key.start:
                left += 1
            array[right] = array[left]
            # print('left',array)
        array[right] = key
        self.quick_sort(array, low, left - 1)
        self.quick_sort(array, left + 1, high)

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if (len(intervals) == 0):
            return []
        # 排序
        self.quick_sort(intervals, 0, len(intervals)-1)
        idx = 0
        retval = []
        curr = intervals[idx]
        
        while idx < len(intervals)-1:
            item = intervals[idx+1]
            if item.start <= curr.end:
                curr = Interval(curr.start, item.end if item.end > curr.end else
                                curr.end)
            else:
                retval.append(curr)
                curr = item
            idx += 1
        retval.append(curr)
        return retval

if __name__ == '__main__':
    a = [Interval(1,4), Interval(0,0)]
    print('input ', a)
    solution = Solution()
    solution.quick_sort(a, 0, len(a)-1)
    # print('output ', a)
    print(solution.merge(a))


# vim: set expandtab ts=4 sts=4 sw=4 :
