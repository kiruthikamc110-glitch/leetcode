# Last updated: 29/09/2026, 21:47:33
1class Solution:
2    def reverseKGroup(self, head, k):
3        dummy = ListNode(0)
4        dummy.next = head
5
6        group_prev = dummy
7
8        while True:
9            kth = group_prev
10
11            for i in range(k):
12                kth = kth.next
13
14                if not kth:
15                    return dummy.next
16
17            group_next = kth.next
18
19            prev = group_next
20            current = group_prev.next
21
22            while current != group_next:
23                next_node = current.next
24                current.next = prev
25                prev = current
26                current = next_node
27
28            temp = group_prev.next
29            group_prev.next = kth
30            group_prev = temp