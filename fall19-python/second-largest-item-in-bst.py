def find_second_largest(root_node):
    
    largest = root_node 
    
    if root_node is None:
        raise(Exception)
    
    if root_node.right is None:
        raise(Exception)
    
    largest = find_largest_pointer(root_node)
    
    if largest.left:
        second = find_largest_pointer(root_node.left)
    
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
