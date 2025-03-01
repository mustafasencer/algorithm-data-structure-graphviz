from data_structures.linked_list import LinkedListNode


def length(node):
    if not node:
        return 0
    length = 0
    while node:
        length += 1
        node = node.next
    return length


def count(node, data):
    if not node:
        return 0
    count = 0
    while node:
        if node.data == data:
            count += 1
        node = node.next
    return count


def push(value) -> None:
    global head
    new_node = LinkedListNode(value)
    new_node.next = head
    head = new_node


if __name__ == "__main__":
    head = None
    for i in range(5, 0, -1):
        push(i)
    count = count(head, 2)
    length = length(head)
