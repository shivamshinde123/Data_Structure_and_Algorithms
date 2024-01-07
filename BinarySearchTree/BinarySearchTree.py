class Node: 
    # Implement a node of the binary search tree.
    # Constructor for a node with key and a given parent
    # parent can be None for a root node.
    def __init__(self, key, parent = None): 
        self.key = key
        self.parent = parent 
        self.left = None # We will set left and right child to None
        self.right = None
        # Make sure that the parent's left/right pointer
        # will point to the newly created node.
        if parent != None:
            if key < parent.key:
                assert(parent.left == None), 'parent already has a left child -- unable to create node'
                parent.left = self
            else: 
                assert key > parent.key, 'key is same as parent.key. We do not allow duplicate keys in a BST since it breaks some of the algorithms.'
                assert(parent.right == None ), 'parent already has a right child -- unable to create node'
                parent.right = self
        
    # Utility function that keeps traversing left until it finds 
    # the leftmost descendant
    def get_leftmost_descendant(self):
        if self.left != None:
            return self.left.get_leftmost_descendant()
        else:
            return self
    
    # TODO: Complete the search algorithm below
    # You can call search recursively on left or right child
    # as appropriate.
    # If search succeeds: return a tuple True and the node in the tree
    # with the key we are searching for.
    # Also note that if the search fails to find the key 
    # you should return a tuple False and the node which would
    # be the parent if we were to insert the key subsequently.
    def search(self, key):
        if self == None or self.key == key: 
            return (True, self)
        # your code here
        if key < self.key:
            left_child_node = self.left
            if left_child_node != None:
                return left_child_node.search(key)
            else:
                return (False, self)
        else:
            right_child_node = self.right
            if right_child_node != None:
                return right_child_node.search(key)
            else:
                return (False, self)
        
    
    #TODO: Complete the insert algorithm below
    # To insert first search for it and find out
    # the parent whose child the currently inserted key will be.
    # Create a new node with that key and insert.
    # return None if key already exists in the tree.
    # return the new node corresponding to the inserted key otherwise.
    def insert(self, key):
        # your code here
        status, parent_node = self.search(key)
        if not status:
            new_node = Node(key, parent_node)
            if new_node.key < parent_node.key:
                parent_node.left = new_node
                new_node.parent = parent_node
                return new_node
            else:
                parent_node.right = new_node
                new_node.parent = parent_node
                return new_node
        else:
            return None

               
        
    # TODO: Complete algorithm to compute height of the tree
    # height of a node whose children are both None is defined
    # to be 1.
    # height of any other node is 1 + maximum of the height 
    # of its children.
    # Return a number that is the height.
    def height(self):
        # your code here
        if self.left == None and self.right == None:
            height = 1
            return height
        else:
            left_child = self.left
            right_child = self.right
            
            if left_child == None:
                left_child_height = 0
            else:
                left_child_height = left_child.height()
                
            if right_child == None:
                right_child_height = 0
            else:
                right_child_height = right_child.height()
            
            height = 1 + max(left_child_height, right_child_height)
            return height
            
        
    
    #TODO: Write an algorithm to delete a key in the tree.
    # First, find the node in the tree with the key.
    # Recommend drawing pictures to visualize these cases below before
    # programming.
    # Case 1: both children of the node are None
    #   -- in this case, deletion is easy: simply find out if the node with key is its
    #      parent's left/right child and set the corr. child to None in the parent node.
    # Case 2: one of the child is None and the other is not.
    #   -- replace the node with its only child. In other words,
    #      modify the parent of the child to be the to be deleted node's parent.
    #      also change the parent's left/right child appropriately.
    # Case 3: both children of the parent are not None.
    #    -- first find its successor (go one step right and all the way to the left).
    #    -- function get_leftmost_descendant may be helpful here.
    #    -- replace the key of the node by its successor.
    #    -- delete the successor node.
    # return: no return value specified
    
    def transplant(self, u, v):
        if u.parent == None:
            self.root = u
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v


        if v != None:
            v.parent = u.parent
            
    def tree_min(self):
        while self.left != None:
            self = self.left
        return self
    
    def delete(self, key):
        (found, node_to_delete) = self.search(key)
        assert(found == True), f"key to be deleted:{key}- does not exist in the tree"
        # your code here
        if node_to_delete.left == None:
            self.transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == None:
            self.transplant(node_to_delete, node_to_delete.left)
        else:
            y = node_to_delete.right.tree_min()
            if y != node_to_delete.right:
                self.transplant(y, y.right)
                y.right = node_to_delete.right
                y.right.parent = y
            self.transplant(node_to_delete, y)
            y.left = node_to_delete.left
            y.left.parent = y


if __name__ == "__main__":

    t1 = Node(25, None)
    t2 = Node(12, t1)
    t3 = Node(18, t2)
    t4 = Node(40, t1)

    print('-- Testing basic node construction (originally provided code) -- ')
    assert(t1.left == t2), 'test 1 failed'
    assert(t2.parent == t1),  'test 2 failed'
    assert(t2.right == t3), 'test 3 failed'
    assert (t3.parent == t2), 'test 4 failed'
    assert(t1.right == t4), 'test 5 failed'
    assert(t4.left == None), 'test 6 failed'
    assert(t4.right == None), 'test 7 failed'
    # The tree should be : 
    #             25
    #             /\
    #         12     40
    #         /\
    #     None  18
    #

    print('-- Testing search -- ')
    (b, found_node) = t1.search(18)
    assert b and found_node.key == 18, 'test 8 failed'
    (b, found_node) = t1.search(25)
    assert b and found_node.key == 25, 'test 9 failed -- you should find the node with key 25 which is the root'
    (b, found_node) = t1.search(26)
    assert(not b), 'test 10 failed'
    assert(found_node.key == 40), 'test 11 failed -- you should be returning the leaf node which would be the parent to the node you failed to find if it were to be inserted in the tree.'

    print('-- Testing insert -- ')
    ins_node = t1.insert(26)
    assert ins_node.key == 26, ' test 12 failed '
    assert ins_node.parent == t4,  ' test 13 failed '
    assert t4.left == ins_node,  ' test 14 failed '

    ins_node2 = t1.insert(33)
    assert ins_node2.key == 33, 'test 15 failed'
    assert ins_node2.parent == ins_node, 'test 16 failed'
    assert ins_node.right == ins_node2, 'test 17 failed'

    print('-- Testing height -- ')

    assert t1.height() == 4, 'test 18 failed'
    assert t4.height() == 3, 'test 19 failed'
    assert t2.height() == 2, 'test 20 failed'

    print('--- All tests passed --- ')

    # Testing deletion
    t1 = Node(16, None)
    # insert the nodes in the list
    lst = [18,25,10, 14, 8, 22, 17, 12]
    for elt in lst:
        t1.insert(elt)

    # The tree should look like this
    #               16
    #            /     \
    #          10      18
    #        /  \     /  \
    #       8   14   17  25
    #          /         /  
    #         12        22


    # Let us test the three deletion cases.
    # case 1 let's delete node 8
    # node 8 does not have left or right children.
    t1.delete(8) # should have both children nil.
    (b8,n8) = t1.search(8)
    assert not b8, 'Test A: deletion fails to delete node.'
    (b,n) = t1.search(10)
    assert( b) , 'Test B failed: search does not work'
    assert n.left == None, 'Test C failed: Node 8 was not properly deleted.'

    # Let us test deleting the node 14 whose right child is none.
    # n is still pointing to the node 10 after deleting 8.
    # let us ensure that it's right child is 14
    assert n.right != None, 'Test D failed: node 10 should have right child 14'
    assert n.right.key == 14, 'Test E failed: node 10 should have right child 14'

    # Let's delete node 14
    t1.delete(14)
    (b14, n14) = t1.search(14)
    assert not b14, 'Test F: Deletion of node 14 failed -- it still exists in the tree.'
    (b,n) = t1.search(10)
    assert n.right != None , 'Test G failed: deletion of node 14 not handled correctly'
    assert n.right.key == 12, f'Test H failed: deletion of node 14 not handled correctly: {n.right.key}'

    # Let's delete node 18 in the tree. 
    # It should be replaced by 22.

    t1.delete(18)
    (b18, n18) = t1.search(18)
    assert not b18, 'Test I: Deletion of node 18 failed'
    assert t1.right.key == 22 , ' Test J: Replacement of node with successor failed.'
    assert t1.right.right.left == None, ' Test K: replacement of node with successor failed -- you did not delete the successor leaf properly?'

    print('-- All tests passed ---')