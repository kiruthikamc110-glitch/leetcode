# Last updated: 29/09/2026, 21:39:04
1class Solution:
2    def removeNthFromEnd(self, head, n):
3        dummy = ListNode(0)
4        dummy.next = head
5
6        slow = dummy
7        fast = dummy
8
9        for i in range(n):
10            fast = fast.next
11
12        while fast.next:
13            slow = slow.next
14            fast = fast.next
15
16        slow.next = slow.next.next
17
18        return dummy.next