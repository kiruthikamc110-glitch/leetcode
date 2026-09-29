# Last updated: 29/09/2026, 21:45:32
1class Solution:
2    def swapPairs(self, head):
3        dummy = ListNode(0)
4        dummy.next = head
5
6        current = dummy
7
8        while current.next and current.next.next:
9            first = current.next
10            second = current.next.next
11
12            first.next = second.next
13            second.next = first
14            current.next = second
15
16            current = first
17
18        return dummy.next