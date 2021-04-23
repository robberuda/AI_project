import moves
import time

goal = 'WWWWGGOOBBRRGGOBRRYYY'

start = 'WRGRBYGYOBYOOWGBWWGRR'

start2mosse= 'WWGGOOBWRRYGYGOWRRBYB'

moves_index = {0:'U', 1:'R', 2:'L', 3:'D', 4:'F', 5:'B'}

#definition of node
class node:
    def __init__(self, value=None, move=None, parent=None):
        self.value = value
        self.move = move
        self.parent = parent  # pointer to parent node in tree
        self.depth = None


#definition of search tree
class search_tree:
    def __init__(self):
        self.root = None
        self.elements = []
        self.leaves = []
        self.max_depth = None
        self.solution = None
        self.solutionNode=None

    def add_root(self, root):
        if self.root == None:
            self.root = root
            self.elements = [root]
            self.leaves = [root]
            self.max_depth = 0
            self.solution = 0

    def get_children(self, father):
        results = [moves.F(father.value), moves.Fp(father.value), moves.R(father.value), moves.Rp(father.value), moves.U(father.value), moves.Up(father.value)]
        children = []
        for i in range(len(results)):
            if results[i] not in self.elements:
                n = node(results[i])
                n.move = moves_index[i]
                n.parent = father
                n.depth = father.depth + 1
                self.elements.append(n)
                self.leaves.append(n)
                if n.depth >= self.max_depth:
                    self.max_depth = n.depth
                if n.value == goal:
                    self.solution = 1
                    self.solutionNode = n
        self.leaves.remove(father)
        
    def print_tree(self):
        print('max depth is: ', self.max_depth)
        for i in range(self.max_depth+1):
            cnt=0
            for el in self.elements:
                if el.depth == i:
                    cnt +=1
            print(i,': ', cnt)

    def expand_tree(self):
        for el in self.leaves:
            if el.depth < 9:
                #print('leaves number: ', len(self.leaves))
                self.get_children(el)
                if (self.solution):
                    print('SOLUTION FOUND')
                    self.print_solution(self.solutionNode)
                    break
            else: break

    def print_solution(self, n):
        for d in range(n.depth):
            print(n.move)
            n = n.parent

#create root node
root = node(start2mosse)
root.depth = 0

#create search tree
tree = search_tree()

#add root
tree.add_root(root)

start_time = time.time()
tree.expand_tree()
print('solved in ' + str(round(time.time() - start_time, 2)) + ' seconds')

#grenerate and print children
tree.print_tree()
