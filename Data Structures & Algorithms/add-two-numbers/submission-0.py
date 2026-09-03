# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        dummy = ListNode()
        curr = dummy

        while l1 or l2:
            if not l1:
                currSum = 0 + l2.val + carry
            elif not l2:
                currSum = l1.val + 0 + carry
            else:
                currSum = l1.val + l2.val + carry
            
            if currSum >= 10:
                carry = 1
            else:
                carry = 0
            
            curr.next = ListNode(currSum%10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry: 
            curr.next = ListNode(carry)
        
        return dummy.next
            
            
                    