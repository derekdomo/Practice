def populate_next_node(root):
    if root == None:
        return None
    if root.left:
        root.left.next = root.right
    if root.next and root.right:
        root.right.next = root.next.left
    populate_next_node(root.left)
    populate_next_node(root.right)
