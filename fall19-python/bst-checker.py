
def is_binary_search_tree(root):

    # Determine if the tree is a valid binary search tree
    
    # use dfs
    
    if root is None:
        return True
    
    nodes = [(root, -float('inf'), float('inf'))]
    
    while len(nodes):
        
        node, lower_bound, upper_bound = nodes.pop()
        
        if (lower_bound >= node.value) or (upper_bound <= node.value):
            return False
        
        if node.left:
            nodes.append((node.left, lower_bound, node.value))
        if node.right:
            nodes.append((node.right, node.value, upper_bound))


    return True
