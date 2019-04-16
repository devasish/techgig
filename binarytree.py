class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def print_level_order(root):

    for h in range(1, height(root) + 1):
        print_given_level(root, h)
        print()



def print_given_level(root, level):

    if root is None: return

    if level == 1:
        print(root.data, end=" ")
    else:
        print_given_level(root.left, level-1)
        print_given_level(root.right, level-1)




def height(root):
    if root == None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1



def main():
    root = Node(1)
    root.left = Node(5)
    root.left.left = Node(4)
    root.left.right = Node(7)
    root.left.left = Node(6)

    root.right = Node(3)
    root.right.left = Node(8)
    root.right.left.left = Node(2)
    root.right.left.left.right = Node(7)
    root.right.left.left.left = Node(3)

    h = height(root)

    print("height  = %s" % h)
    print_level_order(root)


if __name__ == '__main__': main()





