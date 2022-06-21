class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

def longest_path_in_bin_tree(root):
    def recurse(node):
        if not node.left and not node.right:
            return 1, 1
        lt_left = 0
        lp_left = 0
        if node.left:
            lp_left, lt_left = recurse(node.left)
        lt_right = 0
        lp_right = 0
        if node.right:
            lp_right, lt_right = recurse(node.right)

        lt_best = max(lt_left, lt_right)
        lp_best = max(
            lp_left, lp_right, 1 + lt_left + lt_right
        )
        return lp_best, 1 + lt_best

    a, _ = recurse(root)

    return a

if __name__ == "__main__":
    from testing import test_case

    # tree 1
    tree1 = Node(
        Node(
            Node(),
            Node(
                Node(Node(Node())),
                Node(Node(Node()))
            )
        ),
        Node()
    )

    test_case(
        "it should return the length of the longest path through the binary tree",
        longest_path_in_bin_tree(tree1),
        7
    )

    # tree 2
    tree2 = Node(
        Node(
            Node(Node(Node(Node()))),
            Node(
                Node(Node(Node()))
            )
        ),
        Node()
    )

    test_case(
        "it should return the length of the longest path through the binary tree",
        longest_path_in_bin_tree(tree2),
        9
    )

    # tree 2
    tree2 = Node(Node(), Node(Node(Node(Node()))))

    test_case(
        "it should return the length of the longest path through the binary tree",
        longest_path_in_bin_tree(tree2),
        6
    )