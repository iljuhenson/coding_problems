from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ref_list = []
        copy_pointer = (right + left) // 2 + (right + left) % 2 
        start_replacement = copy_pointer
        if (right - left + 1) % 2 == 1:
            start_replacement += 1
        copy_pointer -= 1
        print(f"start_replacement: {start_replacement}")
        print(f"copy_pointer: {copy_pointer}")
        counter = 1
        cp = head
        while cp:
            if counter >= left and counter <= copy_pointer:
                ref_list.append(cp)
                print(f"I appended {counter} element to the ref_list")
            
            if start_replacement <= counter and counter <= right:
                node_to_insert = ref_list.pop()
                node_to_insert.val, cp.val = cp.val, node_to_insert.val
            
            print(f"value of the current node {cp.val}")
            print(f"current counter value {counter}")
            
            cp = cp.next
            counter += 1
            print('-' * 6)
            
        return head


if __name__ == "__main__":
    s = Solution()
    linked_list = ListNode(val=1)
    next_node = linked_list
    for i in range(2, 6):
        next_node.next = ListNode(val=i)
        next_node = next_node.next
    
    left_pos = 1
    right_pos = 1
    ans = s.reverseBetween(linked_list, left_pos, right_pos)

    while ans:
        print(ans.val)
        ans = ans.next

# 1 |2 3 4 5 6|