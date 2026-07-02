#reverse linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

def print_list(head):
    elements = []
    while head:
        elements.append(str(head.val))
        head = head.next
    print(" -> ".join(elements) if elements else "Empty List")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("Original list:")
print_list(head)

solution = Solution()
reversed_head = solution.reverseList(head)

print("Reversed list:")
print_list(reversed_head)
