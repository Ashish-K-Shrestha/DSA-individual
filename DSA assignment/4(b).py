from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def closestValues(root, k, x):
    closest = []
    stack = deque()
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()

        if len(closest) < x:
            closest.append(current.val)
        elif abs(current.val - k) < abs(closest[0] - k):
            closest.pop(0)
            closest.append(current.val)
        else:
            break

        current = current.right

    return closest

# Test
# Creating the binary search tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

k = 3.8
x = 2
result = closestValues(root, k, x)
for num in result:
    print(num, end=" ")
