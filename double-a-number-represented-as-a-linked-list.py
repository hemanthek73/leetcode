# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            if not node:
                return 0
            carry=helper(node.next)
            total=node.val*2+carry
            node.val,carry=total%10,total//10
            return carry
        carry=helper(head)
        if carry:
            new_head=ListNode(carry)
            new_head.next=head
            return new_head
        return head
        