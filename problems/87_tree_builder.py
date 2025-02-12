class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_into_tree(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_tree(root.left, value)
    else:
        root.right = insert_into_tree(root.right, value)
    return root

def serialize_tree(root):
    if root is None:
        return "-"
    left = serialize_tree(root.left)
    right = serialize_tree(root.right)
    return f"({left},{root.value},{right})"

def build_and_serialize_tree(sequence):
    root = None
    for value in sequence:
        root = insert_into_tree(root, value)
    return serialize_tree(root)

# Read input
n = int(input())
sequence = list(map(int, input().split()))

# Build and serialize the tree
result = build_and_serialize_tree(sequence)

# Output the result
print(result)