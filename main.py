import moves
import time
from scipy.spatial.distance import cdist
import numpy as np


goal = 'WWWWGGOOBBRRGGOBRRYYY'

solved = np.array([[1,1,1],[0,1,1],[0,1,0],[1,1,0],[1,0,1],[0,0,1],[1,0,0]]) #noto
#---------------------0-------1-------2-------3-------4-------5-------6-----------

moves_index = {0:'F', 1:'Fc', 2:'R', 3:'Rc', 4:'U', 5:'Uc'}

#definition of node
class node:

    def __init__(self, value=None, move=None, parent=None):
        self.value = value
        self.move = move
        self.parent = parent  # pointer to parent node in tree
        self.depth = None
        self.score = None

    def compute_heuristic(self):
        cubelets = [self.value[0] + self.value[4] + self.value[11],
                    self.value[1] + self.value[5] + self.value[6],
                    self.value[2] + self.value[7] + self.value[8],
                    self.value[3] + self.value[9] + self.value[10],
                    self.value[12] + self.value[17] + self.value[18],
                    self.value[13] + self.value[14] + self.value[19],
                    self.value[15] + self.value[16] + self.value[20]]

        positions = np.empty((0, 3))

        for cubelet in cubelets:
            if 'W' in cubelet:  # is W
                if 'B' in cubelet:  # is B
                    if 'R' in cubelet:  # is R
                        id = 3
                    else:  # is O
                        id = 2
                else:  # is G
                    if 'R' in cubelet:  # is R
                        id = 0
                    else:  # is O
                        id = 1
            else:  # is Y
                if 'B' in cubelet:  # is B
                    if 'R' in cubelet:  # is R
                        id = 6
                    else:  # is O
                        id = 7
                else:  # is G
                    if 'R' in cubelet:  # is R
                        id = 4
                    else:  # is O
                        id = 5
            positions = np.append(positions, [solved[id]], axis=0)

        self.score = sum(np.diag(cdist(solved, positions, metric='cityblock'))) / 4


#definition of search tree
class search_tree:
    def __init__(self, depth_limit=3):
        self.root = None
        self.elements = []
        self.elements_value = []
        self.leaves = []
        self.max_depth = None
        self.solution = None
        self.solutionNode = None
        self.depth_limit = depth_limit + 1

    def add_root(self, root):
        if self.root == None:
            self.root = root
            self.elements = [self.root]
            self.elements_value = [self.root.value]
            self.leaves = [self.root]
            self.max_depth = 0
            self.solution = 0

    def get_children_BF(self, father):
        results = [moves.F(father.value), moves.Fc(father.value), moves.R(father.value), moves.Rc(father.value),
                   moves.U(father.value), moves.Uc(father.value)]
        for i in range(len(results)):
            if results[i] not in self.elements_value:
                n = node(results[i])
                n.move = moves_index[i]
                n.parent = father
                n.depth = father.depth + 1
                self.elements.append(n)
                self.elements_value.append(results[i])
                self.leaves.append(n)
                if n.depth > self.max_depth:
                    self.max_depth = n.depth
                if n.value == goal:
                    self.solution = 1
                    self.solutionNode = n

        self.leaves.remove(father)

    def get_children_DF(self, father):
        results = [moves.F(father.value), moves.Fc(father.value), moves.R(father.value), moves.Rc(father.value),
                   moves.U(father.value), moves.Uc(father.value)]
        children = []

        for i in range(len(results)):
            if results[i] not in self.elements_value:
                n = node(results[i])
                n.move = moves_index[i]
                n.parent = father
                n.depth = father.depth + 1
                self.elements.append(n)
                self.elements_value.append(results[i])
                children.append(n)
                if n.depth > self.max_depth:
                    self.max_depth = n.depth
                if n.value == goal:
                    self.solution = 1
                    self.solutionNode = n

        self.leaves.remove(father)
        #self.elements.remove(father)
        self.leaves = children + self.leaves


    def print_tree(self):
        print('max depth is: ', self.max_depth)
        for i in range(self.max_depth+1):
            cnt=0
            for el in self.elements:
                if el.depth == i:
                    cnt +=1
            print(i,': ', cnt)


    def expand_tree_BF(self):

        while self.max_depth < self.depth_limit:

            self.get_children_BF(self.leaves[0])

            if (self.solution):
                print('\n\n\n\nSOLUTION FOUND: ', end='')
                self.print_tree()
                self.print_solution(self.solutionNode)
                break


    def expand_tree_DF(self):

        while self.max_depth < self.depth_limit:

            if len(self.leaves) != 0:
                if self.leaves[0].depth < self.depth_limit-1:
                    self.get_children_DF(self.leaves[0])
                else:
                    self.leaves.remove(self.leaves[0])
            else: break


            if (self.solution):
                print('\n\n\n\nSOLUTION FOUND: ', end='')
                self.print_tree()
                self.print_solution(self.solutionNode)
                break



    def get_children_Astar(self, father):
        results = [moves.F(father.value), moves.Fc(father.value), moves.R(father.value), moves.Rc(father.value),
                   moves.U(father.value), moves.Uc(father.value)]
        for i in range(len(results)):
            if results[i] not in self.elements_value:
                n = node(results[i])
                n.move = moves_index[i]
                n.parent = father
                n.depth = father.depth + 1
                self.elements.append(n)
                self.elements_value.append(results[i])
                self.leaves.append(n)
                if n.depth > self.max_depth:
                    self.max_depth = n.depth
                if n.value == goal:
                    self.solution = 1
                    self.solutionNode = n

        self.leaves.remove(father)

    def expand_tree_Astar(self): #da fare

        #while len(self.leaves) <=  12:

        while self.max_depth < self.depth_limit:

            results = [moves.F(self.leaves[0].value), moves.Fc(self.leaves[0].value), moves.R(self.leaves[0].value),
                       moves.Rc(self.leaves[0].value), moves.U(self.leaves[0].value), moves.Uc(self.leaves[0].value)]

            for i in range(len(results)):
                if results[i] not in self.elements_value:

                    #create node:
                    n = node(results[i])
                    n.move = moves_index[i]
                    n.parent = self.leaves[0]
                    n.depth = self.leaves[0].depth + 1
                    n.compute_heuristic() # f(n) = h(n)
                    n.score += n.depth # f(n) = g(n) + h(n)

                    print('nodo: ', n.depth,':', n.move, 'score: ', n.score)


                    self.elements.append(n)
                    self.elements_value.append(results[i])


                    for el in range(len(self.leaves)):


                        if el == self.leaves.index(self.leaves[-1]):  # se l'indice corrisponde con l'ultimo elemento
                            self.leaves.append(n)
                            print('LO METTO IN CODA')
                            break


                        elif self.leaves[el].score > n.score:
                            print('iserisco il nodo prima di: ', self.leaves[el].depth,':', self.leaves[el].move, 'score: ', self.leaves[el].score, end=' ')
                            print('e dopo di: ', self.leaves[el-1].depth, ':', self.leaves[el-1].move,'score: ', self.leaves[el-1].score)
                            self.leaves.insert(el, n) #inserendo in posizione "i" sposta l'i-esimo in posizione i+1
                            break

                        else:
                            print('non ho inserito il nodo in posizione ', el)

                        #problema: il nodo viene inserito al posto del root node


                    if n.depth > self.max_depth:
                        self.max_depth = n.depth
                    if n.value == goal:
                        self.solution = 1
                        self.solutionNode = n

            self.leaves.remove(self.leaves[0])

            if (self.solution):
                print('\n\n\n\nSOLUTION FOUND: ', end='')
                self.print_tree()
                self.print_solution(self.solutionNode)
                break






    def print_solution(self, n):
        sol = []
        print('solution is :', end='')
        for d in range(n.depth):
            sol.append(n.move)
            n = n.parent
        sol.reverse()
        print(sol)


    def print_level(self, level):
        print('level', level, ':', end=' ')
        father_move = 'N'
        for el in self.elements:
            if el.depth == level :
                if (level != 0):print(el.parent.move, end='->')
                print(el.move, end=' ')
        print('\n')



start = 'WYBOROGWOWGBGRWBRRYGY'

start2 = 'WWGGOOBWRRYGYGOWRRBYB'

start3 = 'WGGWBWRRYGOOYGOWRRBYB'

start5 = 'GRYWOGWGROBYBYBGWRWRO'

start6 = 'RROWGGWGYGOYRWBBRWBOY'

start8 = 'GOYWRGYGRBRWYWBOGRBOW' #high frequency of front moves



#create root node
root = node(start6)
root.depth = 0
root.score = 0

#create search tree
tree = search_tree(6)

#add root
tree.add_root(root)

start_time = time.time()
tree.expand_tree_Astar()

print('\nworked for ' + str(round(time.time() - start_time, 2)) + ' seconds')

if (tree.solution == 0): tree.print_tree()

