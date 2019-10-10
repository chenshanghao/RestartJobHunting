# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lengthA, lengthB = self.getLinkedListLength(headA), self.getLinkedListLength(headB)
        if lengthA > lengthB:
            for i in range(lengthA - lengthB):
                headA = headA.next
        
        if lengthB > lengthA:
            for i in range(lengthB - lengthA):
                headB = headB.next
        
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
        
    
    def getLinkedListLength(self, head):
        res = 0
        tmp = head
        if not tmp:
            return res
        while tmp:
            res += 1
            tmp = tmp.next
        return res