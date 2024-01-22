# Definition of binary tree
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: TreeNode) -> int:
    res = [0]
    
    def dfs(root):
        if not root:
            return -1
        left = dfs(root.left)
        right = dfs(root.right)
        res[0] = max(res[0], 2 + left + right)

        return 1 + max(left, right)

    dfs(root)
    return res[0]

class TestDiameterOfBinaryTree(unittest.TestCase):
    def test_example_case(self):
        root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertEqual(diameterOfBinaryTree(root1), 3)

    def test_longer_diameter(self):
        root2 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7), TreeNode(8))), TreeNode(3, TreeNode(5), TreeNode(6)))
        self.assertEqual(diameterOfBinaryTree(root2), 5)

    def test_single_node_tree(self):
        root3 = TreeNode(1)
        self.assertEqual(diameterOfBinaryTree(root3), 0)

    def test_only_left_subtree(self):
        root4 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)))
        self.assertEqual(diameterOfBinaryTree(root4), 3)

    def test_only_right_subtree(self):
        root5 = TreeNode(1, None, TreeNode(3, None, TreeNode(6)))
        self.assertEqual(diameterOfBinaryTree(root5), 2)


if __name__ == "__main__":
    unittest.main()

