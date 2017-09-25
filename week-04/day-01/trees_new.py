class Trees(object):
    def __init__(self, type_of_tree, leaf_color, age, sex):
        self.type_of_tree = type_of_tree
        self.leaf_color = leaf_color
        self.age = age
        self.sex = sex

tree_1 = Trees("black birch", "green", "49", "f")
tree_2 = Trees("walnut", "green", "130", "m")
tree_3 = Trees("black oak", "green", "76", "m")
tree_4 = Trees("chestnut", "green", "2", "f")

print(tree_2.age)
print(tree_4.type_of_tree)