# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Решение 1
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB
        countA, countB = 0, 0

        while a:
            countA += 1
            a = a.next

        while b:
            countB +=1
            b = b.next

        if countA > countB:
            c = headA
            diff = countA - countB
            d = headB
        else:
            c = headB
            diff = countB - countA
            d = headA

        i=0
        while i < diff:
            i += 1
            c = c.next

        while c != d:
            c = c.next
            d = d.next

        return c

# Решение 2

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB

        while a != b:
            if not a:
                a = headB
            else:
                a = a.next

            if not b:
                b = headA
            else:
                b = b.next

        return a