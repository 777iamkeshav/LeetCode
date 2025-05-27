# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        t=head

        # take all values into a list

        while t!=None:
            l.append(t.val)
            t=t.next

        # reverse the list 

        l=list(reversed(l))
        t=head
        i=0

        # update linked list data with reversed list
        while(t!=None):
            t.val=l[i]
            i+=1
            t=t.next
        return head