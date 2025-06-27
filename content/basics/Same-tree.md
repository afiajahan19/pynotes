---
title: Same-Tree
date: 2025-06-27
author: Your Name
cell_count: 2
score: 0
---

```python
# Problem: 100. Same Tree
# Checks whether two binary trees are the same

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# Helper function to build a binary tree from a list
def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    front = 0
    index = 1
    while index < len(nodes):
        node = queue[front]
        front += 1
        if index < len(nodes) and nodes[index] is not None:
            node.left = TreeNode(nodes[index])
            queue.append(node.left)
        index += 1
        if index < len(nodes) and nodes[index] is not None:
            node.right = TreeNode(nodes[index])
            queue.append(node.right)
        index += 1
    return root

# Sample trees
tree1 = build_tree([1, 2, 3])
tree2 = build_tree([1, 2, 3])

# Check if both trees are the same
print("Trees are the same:", isSameTree(tree1, tree2))  # Output: True

```

    Trees are the same: True
    


```python

```


---
**Score: 0**