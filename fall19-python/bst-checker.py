def is_binary_search_tree(root):

    # Determine if the tree is a valid binary search tree
    
    # use dfs
    
    if root is None:
        return True
    
    nodes = []
    nodes.append(root)
    
    while len(nodes):
        
        node = nodes.pop()
        
        if (node.left.value > node.value) or (node.right.value < node.value):
            return False
        
        else:
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)


    return True
