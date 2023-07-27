"""
This problem was asked by Amazon.

Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30."""

from data_structures.binary_search_tree import TreeNode, BinarySearchTree

def find_inorder_succesor(t:TreeNode):
    #The inorder successor might be in one of two directions:
    #If the node is a left child, it could be it's parent. If the node has a right child, it might be the child, or the left children of the right child
    node = child_search()
    if node:
        return node
    node = parent_search()
    if node:
        return node
    else:
        return None
    
def child_search(t:TreeNode)->TreeNode:
    if t.get_right_child():
        curr_node = t.get_right_child()
        while curr_node.get_left_child():
            curr_node = curr_node.get_left_child()
        return curr_node
    return None

def parent_search(t:TreeNode):
    if t.is_left_child():
        curr_node = t.parent()
        return curr_node
    return None