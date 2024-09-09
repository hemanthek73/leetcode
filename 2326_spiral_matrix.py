# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        def insideMatrixAndNotused(i,j):
            return (0<=i<m) and (0<=j<n) and (matrix[i][j]==-1)
        matrix=[[-1 for _ in range(n)] for _ in range(m)]
        i,j=0,0
        diri,dirj=0,1
        while head:
            matrix[i][j]=head.val
            head=head.next

            nexti=i+diri
            nextj=j+dirj
            if insideMatrixAndNotused(nexti,nextj):
                i=nexti
                j=nextj
            else:
                diri,dirj=dirj,-diri
                i+=diri
                j+=dirj
                if not insideMatrixAndNotused(i,j):
                    break
        return matrix       