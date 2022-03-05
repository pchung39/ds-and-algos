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

def reverse_sub_list(head, p, q):
    
    # edge case
    if p == q:
        return head 
    
    current = head 
    prev = None 
    p_prev = None 

    while current != None:

        if current == p:
            p_prev = prev
            next = current.next 
            current.next = prev
            prev = current 
            current = next 

        else:
            continue  
        
        if current == q:

            # need to connect p to q.next

            # need to connect q to p-1 

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ")
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ")
    result.print_list()


main()