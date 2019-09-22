# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        oddHead = oddTmp = ListNode(-1)
        evenHead = evenTmp = ListNode(-1)
        while True:
            oddTmp.next = head
            head = head.next
            oddTmp = oddTmp.next
            oddTmp.next = None
            
            evenTmp.next = head
            head = head.next
            evenTmp = evenTmp.next
            evenTmp.next = None
            
            if not head or not head.next:
                break
        if head:
            oddTmp.next = head
            oddTmp = oddTmp.next
        oddTmp.next = evenHead.next
        return oddHead.next
            
        