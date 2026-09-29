# Last updated: 29/09/2026, 21:40:20
1class Solution:
2    def mergeTwoLists(self, list1, list2):
3        dummy = ListNode(0)
4        current = dummy
5
6        while list1 and list2:
7            if list1.val <= list2.val:
8                current.next = list1
9                list1 = list1.next
10            else:
11                current.next = list2
12                list2 = list2.next
13
14            current = current.next
15
16        if list1:
17            current.next = list1
18        else:
19            current.next = list2
20
21        return dummy.next