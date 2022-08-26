class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child): # laptop
        child.parent = self # root
        print(self.parent)
        # laptop.parent = root
        self.children.append(child) # root.children.append(laptop)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    root.add_child(laptop)
    root.print_tree()
    return root


if __name__ == '__main__':
    root = build_product_tree()
    pass