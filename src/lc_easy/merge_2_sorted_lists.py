# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def convert_to_nodelist(lst):
            node_list = []
            print(lst)
            lst = lst[::-1]
            print(lst)
            for i, num in enumerate(lst):
                val = num
                if i == len(lst) - 1:
                    next = None
                    node_list.append(ListNode(val=val, next=next))
                else:
                    next = node_list[0]
                    node_list.insert(0, ListNode(val=val, next=next))

        # node_list_1 = convert_to_nodelist(list1)
        # node_list_2 = convert_to_nodelist(list2)
        # print(node_list_1, node_list_2)
            # node_list = [ ListNode(lst[i], next=) ]

        merged = []
        for i in list1[::]:
            merged.append(list1.pop(i))
            for j in list2[::]:
                if j >= i:
                    merged.append(list2.pop(j))
                #     merged.append(i)
                # else:
                #     merged.append(j)
                # elif i > j:
                #     merged.append(j)
                # else:
                #     continue
        print(merged)
        return merged

def test(input, expected):
    list1, list2 = input
    # print(list1)
    # print(list2)
    # print(expected)
    return Solution().mergeTwoLists(list1, list2) == expected

test_cases = [
    {
        'input': ([1,2,4], [1,3,4]),
        'expected': [1,1,2,3,4,4]
    },
    {
        'input': ([], []),
        'expected': []
    },
    {
        'input': ([], [0]),
        'expected': [0]
    }
]

for test_case in test_cases:
    res = test(test_case['input'], test_case['expected'])
    print('PASSED' if res else 'FAILED')