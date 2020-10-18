# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.num_to_node(self.node_to_num(l1) + self.node_to_num(l2))
    
    def node_to_num(self, node: ListNode) -> int:
        num = 0
        place = 0
        while node:
            num += node.val * 10 ** place
            node = node.next
            place += 1
        return num
    
    def num_to_node(self, num: int) -> ListNode:
        first = node = ListNode(num % 10)
        num //= 10
        while num > 0:
            new_node = ListNode(num % 10)
            node.next = new_node
            node = new_node
            num //= 10
        return first
