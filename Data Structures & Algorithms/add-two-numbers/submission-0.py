# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        h1, h2 = l1, l2
        res1 = ""
        res2 = ""

        while h1:
            res1 += str(h1.val)
            h1 = h1.next 
        
        while h2:
            res2 += str(h2.val)
            h2 = h2.next
        
        result1 = int(res1[::-1])
        result2 = int(res2[::-1])

        final_result = str(result1 + result2)

        fin = (final_result[::-1])
        list(fin)

        dummy = ListNode(0)
        head = dummy 

        for i in range(len(fin)):
            new_node = ListNode()
            new_node.val = int(fin[i])
            head.next = new_node
            head = head.next
        return dummy.next
        
    
        