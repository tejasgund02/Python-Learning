# Tree in python

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, node):
        node.parent = self
        self.children.append(node)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def define_tree():
    root = TreeNode("data Structure")

    tree_node1 = TreeNode("Lenear Data Structure")
    tree_node1.add_child(TreeNode("Stack"))
    tree_node1.add_child(TreeNode("Queue"))
    tree_node1.add_child(TreeNode("Array"))
    tree_node1.add_child(TreeNode("Linked List"))


    tree_node2 = TreeNode("Non Lenear Data Structure")
    tree_node2.add_child(TreeNode("Tree"))
    tree_node2.add_child(TreeNode("Graph"))


    root.add_child(tree_node1)
    root.add_child(tree_node2)

    root.print_tree()

# Example usage
if __name__ == "__main__":  
    define_tree()