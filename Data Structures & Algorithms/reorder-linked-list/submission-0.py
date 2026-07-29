# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast and slow pointer
        # split up into two groups
        # reverse the second one
        # and then group one followed by group two

        if not head:
            return None 

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #now slow should be at the midpoint
        #fast should be at the end

        second = slow.next
        slow.next = None

        #reverse l2
        prev = None
        curr = second

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        first = head
        second = prev

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
        
        return
        
        

