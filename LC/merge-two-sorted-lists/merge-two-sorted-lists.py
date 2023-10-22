# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create dummy node
        dummy = ListNode(-1)
        current = dummy

        # Traverse both linked lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            # Move to the last node in merged list
            current = current.next

        # If one of the linked lists is not exhausted, append it
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next  # Skip dummy node


list1 = [1,2,4]
list2 = [1,3,4]
solution = Solution()
result = solution.mergeTwoLists(list1, list2)
print(result)