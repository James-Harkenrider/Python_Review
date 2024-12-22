
# class AddNumbers:
#
#     def __init__(self, num1: int, num2: int):
#         self.num1 = num1
#         self.num2 = num2
#
#     def add_values(self):
#         sum_values = self.num1 + self.num2
#         return sum_values
#
#
# addObj = AddNumbers(num1=1, num2=2)
# print(addObj.add_values())

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode{{val: {self.val}, next: {repr(self.next)}}}'


# Example usage:
node3 = ListNode(3)
node2 = ListNode(4, node3)
node1 = ListNode(2, node2)

print(node1.next.next)