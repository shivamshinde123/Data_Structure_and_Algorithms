# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        # Finding the middle node (middle node will be represented by the variable named slow at the end of the while loop)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reversing the middle element + second half of the linked list
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 becomes 1 -> 2 -> 3 -> 4 <- 5 <- 6 <- 7
        # After the completion of while loop, the variable named prev will represent the last node of the linked list
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # Now we will compare corresponding node values using two variables namely head and prev
        while prev:
            if head.val != prev.val:
                return False
                
            head = head.next
            prev = prev.next
            
        return True
            
        