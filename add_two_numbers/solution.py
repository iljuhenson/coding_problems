# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_on_num = 0
        ans = None
        last_ans_node = ListNode

        while True:
            if not l1 and not l2 and carry_on_num == 0:
                break
            

            last_ans_node.next = ListNode()
            last_ans_node = last_ans_node.next
            
            if not ans:
                ans = last_ans_node

            if not l1:
                l1 = ListNode()

            if not l2:
                l2 = ListNode()
            
            sum = carry_on_num + l1.val + l2.val

            carry_on_num = sum // 10
            last_ans_node.val = sum % 10
            
            l1 = l1.next
            l2 = l2.next

        return ans

