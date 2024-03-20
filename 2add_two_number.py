class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        Head=ListNode(0)
        tail=Head
        carry=0
        while l1 is not None or l2 is not None or carry!=0:
            dig1=l1.val if l1 is not None else 0
            dig2=l2.val if l2 is not None else 0
            sum=dig1+dig2+carry
            dig=sum%10
            carry=sum//10
            newNode=ListNode(dig)
            tail.next=newNode
            tail=tail.next
            l1=l1.next if l1 is not None else None
            l2=l2.next if l2 is not None else None
        res=Head.next
        Head.next=None
        return res
        