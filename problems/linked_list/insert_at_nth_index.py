from data_structures.linked_list import LinkedListNode, print_linked_list
from problems.linked_list.build_linked_list import build_linked_list


def insert_nth(head_node, index, data):
    # Return the head of the list.
    head = head_node
    if not head_node:
        head = LinkedListNode(data)
        return head
    if index < 1:
        new_node = LinkedListNode(data)
        new_node.next = head_node
        head = new_node
        return head
    while index > 0:
        if index == 1:
            new_node = LinkedListNode(data)
            new_node.next = head_node.next
            head_node.next = new_node
            break
        head_node = head_node.next
        index -= 1
    if index != 1:
        print("List index out of range")
    return head


def insert_nth_(head_node, index, data):
    head = head_node
    if not head_node:
        head = head_node
        return head

    if index < 1:
        new_node = LinkedListNode(data)
        new_node.next = head_node
        head = new_node
        return head

    while index > 0:
        if index == 1:
            new_node = LinkedListNode(data)
            new_node.next = head_node.next
            head_node.next = new_node
            break
        head_node = head_node.next
        index -= 1

    return head


def insert_nth__(head, index, data):
    return (
        LinkedListNode(data, head)
        if not index
        else LinkedListNode(head.data, insert_nth__(head.next, index - 1, data))
    )


if __name__ == "__main__":
    INDEX = 3
    VALUE = 100
    RANGE = 5
    nums = [i for i in range(RANGE)]
    head = build_linked_list(nums)
    result = insert_nth_(head, INDEX, VALUE)
    print_linked_list(result)
