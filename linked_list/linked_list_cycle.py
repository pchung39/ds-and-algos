class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):

    # initialize needed variables
    slow = head 
    fast = head

    # what is the boundaries we need to run this logic?
    # for this: fast and the next fast node can't be None
    while fast is not None and fast.next is not None:
        
        # increment both fast and slow pointers
        slow = slow.next 
        fast = fast.next.next 

        # check if slow and fast pointers are in the same point, if yes then return True 
        if slow == fast:
            return True 
    
    # if we are at this point, then a cycle was not found within the boundaries of the linked list, 
    # so return False   
    return False 

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))


main()