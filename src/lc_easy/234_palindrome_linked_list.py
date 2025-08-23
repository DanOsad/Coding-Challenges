# https://leetcode.com/problems/palindrome-linked-list/

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        curr_node = head
        while curr_node != None:
            vals.append(curr_node.val)
            curr_node = curr_node.next

        i = 0
        j = len(vals) - 1

        while i < j:
            if vals[i] == vals[j]:
                i += 1
                j -= 1
            else:
                return False
        return True