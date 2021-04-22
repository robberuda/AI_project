import moves


class node:
    def __init__(self, value=None):
        self.value = value
        self.move = None
        self.parent = None  # pointer to parent node in tree


class search_tree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        self.root == None:
            self.root = node

    def generate_child_of(self, node):
        #




goal = 'WWWWGGRRBBOOGGRRBBOOYYYY'

start = 'WBROWBYOWGRBGWGRBRYOYOGY'


root = node()
root = node(start)

tree = search_tree()
tree.insert(root)





def get_moves(pos):
    return [moves.U(pos), moves.R(pos), moves.L(pos), moves.D(pos), moves.F(pos), moves.B(pos)]


# depth limited:
def findSolution(pos):
    if (pos == goal): return "it's already the solution"


print(tree.root.value)
