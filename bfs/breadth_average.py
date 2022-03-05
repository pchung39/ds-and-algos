from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):

    result = []
    queue = deque()
    queue.append(root)

    while queue:

        current_level = []

        for _ in range(len(queue)):

            current_node = queue.popleft()
            current_level.append(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            
        # calculate the average 
        average = sum(current_level)/ len(current_level)
        result.append(average)

    return result




def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()


[[1], [2, 3], [4,5]]