# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        rlist = ListNode()
        r = rlist

        while list1 and list2:
            if list1.val < list2.val:
                r.next = list1
                list1 = list1.next
            else:
                r.next = list2
                list2 = list2.next
            r = r.next

        if list1:
            r.next = list1
        elif list2:
            r.next = list2

        return rlist.next