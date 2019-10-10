# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        tmp = dummy 
        carry = 0
        
        while l1 or l2:
            tmp_value = 0
            if l1:
                tmp_value += l1.val
                l1 = l1.next
            if l2:
                tmp_value += l2.val
                l2 = l2.next
            tmp_value += carry
            val = tmp_value % 10
            carry = tmp_value // 10
            tmp.next = ListNode(val)
            tmp = tmp.next
        
        if carry:
            tmp.next = ListNode(carry)
            
        return dummy.next