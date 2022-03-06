class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# def find_path(root, sequence):

#     return find_sequences(root, sequence, [])
    
# def find_sequences(current_node, target, current_sequence):

#     # at this point, the target sequence has not been met and there are no additional
#     # nodes to process, therefore, this path is False
#     if current_node is None:
#         return False
    
#     # add current node value to current sequence 
#     current_sequence.append(current_node.val)
#     print(current_sequence)
#     # determine if current sequence is equal to target sequence, make sure that left and right nodes are ended too
#     # if it is, then append the set to true
#     if current_sequence == target and current_node.left is None and current_node.right is None:
#         return True
    
#     # recursively traverse through the tree, 
#     return find_sequences(current_node.left, target, current_sequence) or find_sequences(current_node.right, target, current_sequence)

def find_path(root, sequence):
  if not root:
    return len(sequence) == 0

  return find_path_recursive(root, sequence, 0)


def find_path_recursive(currentNode, sequence, sequenceIndex):

  if currentNode is None:
    return False

  # instead of taking the list approach of appending values to a list. we can directly comapare the current node value 
  # with the the index on the target sequence.
  # we are also checking to make sure that the sequence index does not go ovcer the target sequence length. If it does
  # return false
  seqLen = len(sequence)
  if sequenceIndex >= seqLen or currentNode.val != sequence[sequenceIndex]:
    return False

  # if the current node is a leaf, add it is the end of the sequence, we have found 
  # a path!
  if currentNode.left is None and currentNode.right is None \
                              and sequenceIndex == seqLen - 1:
    return True

  # recursively call to traverse the left and right sub-tree
  # return true if any of the two recursive call return true
  return find_path_recursive(currentNode.left, sequence, sequenceIndex + 1) or \
         find_path_recursive(currentNode.right, sequence, sequenceIndex + 1)



def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()