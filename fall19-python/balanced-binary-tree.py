def is_balanced(tree_root):

    # Determine if the tree is superbalanced
    
    # is dfs or bfs appropriate here? dfs
    
    if tree_root is None:
        return True
    
    depths = []
    dfs = []
    dfs.append((tree_root,0))
    
    while len(dfs):
        
        node, depth = dfs.pop()
        
        if (node.left is None) and (node.right is None):
            
            if depth not in depths:
                depths.append(depth)
        
        
            if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                return False
            
        else:
            if node.left:
                dfs.append((node.left, depth+1))
            if node.right:
                dfs.append((node.right, depth+1))


    return True
