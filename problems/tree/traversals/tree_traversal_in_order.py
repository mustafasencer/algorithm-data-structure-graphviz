from data_structures.tree import TreeNode
from problems.tree.builds.build_tree_level_order import build_tree


def recursion(root: TreeNode):
    result = []

    def helper(root) -> None:
        if root:
            helper(root.left)
            result.append(root.val)
            helper(root.right)

    helper(root)
    return result


def stack(root: TreeNode):
    current = root
    stack = []
    result = []

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            result.append(current.val)
            current = current.right
    return result


def stack_v2(root: TreeNode):
    if not root or not root.val:
        return None
    stack = []
    result = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.val)
        root = root.right
    return result


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(array, len(array))
    result = stack(root)
    result_ = recursion(root)
    assert result == result_
