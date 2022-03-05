# class LinkedList(object):

#     def __init__(self, head, tail):

#         self.head = head
#         self.tail = tail

#     def walk(self):

#         pointer = self.head

#         while pointer != None:
#             print(pointer.key)
#             pointer = pointer.next
        
#         print("End of list")

# class Node(object):

#     def __init__(self, key, next_node=None):

#         self.key = key
#         self.next = next_node 
    
#     def add_next(self, node):

#         self.next = node


# first_node = Node(10)
# next_node = Node(20)
# first_node.add_next(next_node)
# linked = LinkedList(first_node, None)

# linked.walk()

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print()

def reverse_list(head):

    current = head 
    previous = None 

    while current != None:
        next_node = current.next 
        current.next = previous
        # bump everything up one 
        previous = current 
        current = next_node

    return previous



def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ")
    head.print_list()
    result = reverse_list(head)
    print("Nodes of reversed LinkedList are: ")
    result.print_list()


main()

