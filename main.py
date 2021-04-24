import moves
import time

goal = 'WWWWGGOOBBRRGGOBRRYYY'


moves_index = {0:'F', 1:'Fc', 2:'R', 3:'Rc', 4:'U', 5:'Uc'}
#moves_index = {0:'Fc', 1:'Rc', 2:'Uc'}

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
        self.elements_value = []
        self.leaves = []
        self.max_depth = None
        self.solution = None
        self.solutionNode = None
        self.semi_solution = None

    def add_root(self, root):
        if self.root == None:
            self.root = root
            self.elements = [self.root]
            self.elements_value = [self.root.value]
            self.leaves = [self.root]
            self.max_depth = 0
            self.solution = 0

    def get_children(self, father):
        results = [moves.F(father.value), moves.Fc(father.value), moves.R(father.value), moves.Rc(father.value), moves.U(father.value), moves.Uc(father.value)]
        #results = [moves.Fp(father.value), moves.Rp(father.value),  moves.Up(father.value)]
        children = []
        for i in range(len(results)):
            if results[i] not in self.elements_value:
                n = node(results[i])
                n.move = moves_index[i]
                n.parent = father
                n.depth = father.depth + 1
                self.elements.append(n)
                self.elements_value.append(results[i])
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
                    print('SOLUTION FOUND: ', end='')
                    self.print_tree()
                    self.print_solution(self.solutionNode)
                    break
            else: break

    def print_solution(self, n):
        sol = []
        for d in range(n.depth):
            sol.append(n.move)
            #print(n.move, end = '<-->')
            n = n.parent
        sol.reverse()
        print (sol)




start = 'RYWRORBRGYGYORBWBWGWO'

start2 = 'WWGGOOBWRRYGYGOWRRBYB'

start3 = 'WGGWBWRRYGOOYGOWRRBYB'

start5 = 'GRYWOGWGROBYBYBGWRWRO'

start6 = 'RROWGGWGYGOYRWBBRWBOY'





#create root node
root = node(start6)
root.depth = 0

#create search tree
tree = search_tree()

#add root
tree.add_root(root)


start_time = time.time()
tree.expand_tree()
print('\nworked for ' + str(round(time.time() - start_time, 2)) + ' seconds')
if (tree.solution == 0): tree.print_tree()

