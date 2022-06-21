class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return f'{self.value}, {self.next if self.next else ""}'

def move_to_end(value, head):
    if not head:
        return
    cursor = head.next
    prev = head 
    to_end = head if prev.value == value else None
    if to_end:
        head = cursor
    while cursor:
        if cursor.value == value:
            to_end = cursor
            prev.next = cursor.next
        
        prev = cursor
        cursor = cursor.next
    prev.next = to_end
    if to_end:
        to_end.next = None
    return head


def make(val):
    if val is None or len(val) == 0:
        return None
    head = Node(val[0], None)
    cursor = head
    for i in range(1, len(val)):
        cursor.next = Node(val[i], None)
        cursor = cursor.next

    return head

def test(expectation: Node, actual: Node):
    if str(expectation) == str(actual):
        print(f'passed! {str(expectation)} == {str(actual)}' )
        return
    print(f"{str(expectation)} != {str(actual)}")
    return

# 1
test(make(list()), make(list()))
# 2
test(make([2, 3, 7]), make([2, 3, 7]))
# 3
expectation = make([3, 2, 7])
actual = move_to_end(7, make([3, 7, 2]))
test(expectation, actual)
