# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        tmp = dummy
        carry = 0
        
        while l1 or l2:
            tmpVal = 0
            if l1:
                tmpVal += l1.val
                l1 = l1.next
            if l2:
                tmpVal += l2.val
                l2 = l2.next
            tmpVal += carry
            val = tmpVal % 10
            carry = tmpVal // 10
            tmp.next = ListNode(val)
            tmp = tmp.next
        if carry:
            tmp.next = ListNode(carry)
        return dummy.next 
        
        
            
            
        