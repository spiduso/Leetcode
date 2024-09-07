"""
https://leetcode.com/problems/linked-list-in-binary-tree
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_sub_path_dfs(self, head, root):
        # head already found
        if not head:
            return True

        # head can't be found
        if not root or head.val != root.val:
            return False

        # recursively try both subtrees
        return self.is_sub_path_dfs(head.next, root.left) or self.is_sub_path_dfs(head.next, root.right)

    def isSubPath(self, head, root):
        if not root:
            return False

        if self.is_sub_path_dfs(head, root):
            return True

        # try again with subtrees without root
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


if __name__ == "__main__":
    print((Solution()).isSubPath(ListNode(2, ListNode(2, ListNode(1))),
                                 TreeNode(2, None, TreeNode(2, None, TreeNode(2, None, TreeNode(1))))))
