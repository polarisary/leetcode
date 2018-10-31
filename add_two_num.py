# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i1 = str(l1.val)
        while l1.next:
            l1 = l1.next
            i1 += str(l1.val)
        i2 = str(l2.val)
        while l2.next:
            l2 = l2.next
            i2 += str(l2.val)
        i1 = int(i1[::-1])
        i2 = int(i2[::-1])
        i3 = i1 + i2
        l3 = str(i3)[::-1]
        print(l3)
        return self.str2Node(l3)

    def str2Node(self, s):
        node = ListNode(s[0])
        # 尾指针
        tail = node
        tmp = s[1:]
        for l in tmp:
            n = ListNode(l)
            tail.next = n
            tail = n
        return node


if __name__ == '__main__':
    l2 = ListNode(2)
    l4 = ListNode(4)
    l2.next = l4
    l3 = ListNode(3)
    l4.next = l3

    l5 = ListNode(5)
    l6 = ListNode(6)
    l5.next = l6
    l7 = ListNode(4)
    l6.next = l7
    s = Solution()
    s.addTwoNumbers(l2, l5)
