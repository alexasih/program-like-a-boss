def find_second_largest(root_node):
    
    largest = root_node 
    
    if root_node is None or (root_node.right is None and root_node.left is None):
        raise(Exception)
    
    if root_node.left is not None and root_node.right is None:
        return root_node.left.value
    
    largest = find_largest_pointer(root_node)
    
    if largest.left:
        return find_largest_pointer(largest.left).value
    
    else:
        return find_node_before_largest(root_node).value
        



def find_largest_pointer(root_node):
    
    current = root_node
    
    while current:
        if not current.right:
            return current
            
        current = current.right
        

def find_node_before_largest(root_node):
    
    current = root_node
    
    while current:
        if not current.right.right:
            return current
            
        current = current.right
