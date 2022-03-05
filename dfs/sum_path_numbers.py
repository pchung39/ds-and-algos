class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_sum_of_path_numbers(root):

    return traverse_paths(root, 0)

def traverse_paths(current, sum):

    # base case
    if current is None:
        return 0
    
    # calculate the sum 
    sum = sum * 10 + current.val

    # if there are no other left and right nodes to traverse, return the sum 
    if current.left is None and current.right is None:
        return sum

    # recursive solution for both left and right nodes 
    # TODO: got this logic wrong
    return traverse_paths(current.left, sum) + traverse_paths(current.right, sum)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()