from typing import Optional

class Node:
    def __init__(self, value: int, next: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next

    def to_string(self) -> str:
        s = str(self.value)
        curr = self
        while curr.next:
            s = f'{s} > {curr.next.value}'
            curr = curr.next
        return s

def reverse_list(head: Node) -> Node:
    previous = None
    current = head
    while current:
        tmp_next = current.next
        current.next = previous
        previous = current
        current = tmp_next

    if previous is None:
        raise ValueError("Cannot reverse an empty list")

    return previous

def test_reversal():
    head = Node(2)
    head.next = Node(5)
    head.next.next = Node(7)
    head.next.next.next = Node(15)

    assert head.to_string() == '2 > 5 > 7 > 15'
    assert reverse_list(head).to_string() == '15 > 7 > 5 > 2'
