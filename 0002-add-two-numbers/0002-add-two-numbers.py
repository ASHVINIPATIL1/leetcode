# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            node1 = l1
            node2 = l2
            s1 = ''
            s2 = ''

            while node1:
                s1 = s1 + str(node1.val)
                node1 = node1.next

            while node2:
                s2 = s2 + str(node2.val)
                node2 = node2.next

            s1 = s1[::-1]
            s2 = s2[::-1]

            num = int(s1)+int(s2)

            rev = str(num)[::-1]

            dummy = ListNode(0)
            current = dummy

            for i in rev:
                current.next = ListNode(int(i))
                current = current.next
                
            return dummy.next
            

            
        