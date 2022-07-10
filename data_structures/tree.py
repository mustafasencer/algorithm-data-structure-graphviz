class TreeNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


class TreeNodeWithChildren:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes
