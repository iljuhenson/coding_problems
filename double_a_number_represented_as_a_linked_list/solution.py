# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        
        head_copy = head
        while head_copy:
            new_value = head_copy.val * 2
           
            tenth = new_value // 10
            ones = new_value % 10
            
            head_copy.val = ones

            if tenth != 0:
                if not prev:
                    head = ListNode(tenth, head_copy)
                else:
                    prev.val += tenth

            prev = head_copy
            head_copy = head_copy.next
        return head
