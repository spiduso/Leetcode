"""
https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# classic binary search
def is_in_arr(arr, num):
    left_i = 0
    right_i = len(arr) - 1
    pivot = (right_i + left_i) // 2

    if num == arr[left_i] or num == arr[right_i]:
        return True

    while left_i + 1 < right_i:
        if num == arr[pivot]:
            return True

        if num < arr[pivot]:
            right_i = pivot
        else:
            left_i = pivot

        pivot = (right_i + left_i) // 2

    return False


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums.sort()

        processed = {}
        result_head = None

        # find head for result
        while head is not None and result_head is None:
            # save processed numbers
            if head.val in processed:
                result = processed[head.val]
            else:
                result = is_in_arr(nums, head.val)
                processed[head.val] = result

            if not result:
                result_head = head
            else:
                head = head.next

        if result_head is None:
            return None

        # head found, now just remove next values
        while head.next is not None:
            if head.next.val in processed:
                result = processed[head.next.val]
            else:
                result = is_in_arr(nums, head.next.val)
                processed[head.next.val] = result

            if result:
                head.next = head.next.next
            else:
                head = head.next

        return result_head


if __name__ == "__main__":
    print(Solution().modifiedList([1, 2, 3], ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
