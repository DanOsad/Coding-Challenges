# https://leetcode.com/problems/linked-list-cycle

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        curr = head
        while curr:
            if curr not in visited:
                visited.append(curr)
                curr = curr.next
            else:
                return True
        return False