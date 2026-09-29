# Last updated: 29/09/2026, 21:44:08
1class Solution:
2    def mergeKLists(self, lists):
3        if not lists:
4            return None
5
6        while len(lists) > 1:
7            merged = []
8
9            for i in range(0, len(lists), 2):
10                list1 = lists[i]
11                
12                if i + 1 < len(lists):
13                    list2 = lists[i + 1]
14                else:
15                    list2 = None
16
17                merged.append(self.mergeTwoLists(list1, list2))
18
19            lists = merged
20
21        return lists[0]
22
23    def mergeTwoLists(self, list1, list2):
24        dummy = ListNode(0)
25        current = dummy
26
27        while list1 and list2:
28            if list1.val <= list2.val:
29                current.next = list1
30                list1 = list1.next
31            else:
32                current.next = list2
33                list2 = list2.next
34
35            current = current.next
36
37        if list1:
38            current.next = list1
39        else:
40            current.next = list2
41
42        return dummy.next