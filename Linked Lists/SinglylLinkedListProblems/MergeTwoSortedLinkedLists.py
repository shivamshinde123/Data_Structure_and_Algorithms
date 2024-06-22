# You are given the heads of two sorted linked lists list1 and list2. 

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.   

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # This is quite like the code from merge sort
        head = ListNode(-1)
        prev = head
        while l1 and l2:
            if l1.val <= l2.val:
                new_node = ListNode(l1.val)
                prev.next = new_node
                l1 = l1.next
            else:
                new_node = ListNode(l2.val)
                prev.next = new_node
                l2 = l2.next
            
            prev = prev.next
            
        while l1:
            new_node = ListNode(l1.val)
            prev.next = new_node
            l1 = l1.next
            prev = prev.next
            
        while l2:
            new_node = ListNode(l2.val)
            prev.next = new_node
            l2 = l2.next
            prev = prev.next
        
        return head.next
            
            
            
            
            
            