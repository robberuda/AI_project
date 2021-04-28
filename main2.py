import moves2
import time
from scipy.spatial.distance import cdist
import numpy as np

goal = 'WWWWGGOOBBRRGGOBRRYYY'

solved = np.array([[1,1,1],[0,1,1],[0,1,0],[1,1,0],[1,0,1],[0,0,1],[1,0,0]]) #noto
#---------------------0-------1-------2-------3-------4-------5-------6-----------


# definition of node ---------------------------------------------------------------------------------------------------
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




# definition of search tree --------------------------------------------------------------------------------------------
class search_tree:
    def __init__(self, root = None, depth_limit = 3):
        self.root = root
        self.elements = [self.root]
        self.elements_value = [self.root.value]
        self.leaves = [self.root]
        self.max_depth = 0
        self.solution = 0
        self.solutionNode = None
        self.depth_limit = depth_limit + 1


    def print_solution(self,nod):
        sol = []
        print('\nsolution is :', end='')
        for d in range(nod.depth):
            sol.append(nod.move)
            nod = nod.parent
        sol.reverse()
        for s in range(len(sol)):
            print(' -> ', sol[s], end='')


    def print_solution_reverse(self, nod): #used only for bidirectional search, from node to goal
        for d in range(nod.depth):
            print(' -> ',moves2.moves_index_reverse[nod.move], end='')
            nod = nod.parent



    def print_level(self, level):
        print('level', level, ':', end=' ')
        for el in self.elements:
            if el.depth == level :
                if (level != 0):print(el.parent.move, end='->')
                print(el.move, end=' ')
        print('\n')

    def print_tree(self):
        for i in range(self.max_depth+1):
            cnt=0
            for el in self.elements:
                if el.depth == i:
                    cnt +=1
            print(i,': ', cnt)


    def expand_tree_BF(self, n):

        self.depth_limit = n

        while self.max_depth < self.depth_limit:

            results = [moves2.F(self.leaves[0].value), moves2.Fc(self.leaves[0].value), moves2.R(self.leaves[0].value),
                       moves2.Rc(self.leaves[0].value), moves2.U(self.leaves[0].value), moves2.Uc(self.leaves[0].value)]

            for i in range(len(results)):
                if results[i] not in self.elements_value:
                    n = node(results[i])
                    n.move = moves2.moves_index[i]
                    n.parent = self.leaves[0]
                    n.depth = self.leaves[0].depth + 1
                    self.elements.append(n)
                    self.elements_value.append(results[i])
                    self.leaves.append(n)
                    if n.depth > self.max_depth:
                        self.max_depth = n.depth
                    if n.value == goal:
                        self.solution = 1
                        print('\n\t--- SOLUTION FOUND! ---\n')
                        self.print_tree()
                        self.print_solution(n)
                        return None


            self.leaves.remove(self.leaves[0])



    def expand_tree_Astar(self): #da fare

        while self.max_depth < self.depth_limit:

            results = [moves2.F(self.leaves[0].value), moves2.Fc(self.leaves[0].value), moves2.R(self.leaves[0].value),
                       moves2.Rc(self.leaves[0].value), moves2.U(self.leaves[0].value), moves2.Uc(self.leaves[0].value)]

            for i in range(len(results)):
                if results[i] not in self.elements_value:

                    #create node:
                    n = node(results[i])
                    n.move = moves2.moves_index[i]
                    n.parent = self.leaves[0]
                    n.depth = self.leaves[0].depth + 1
                    n.compute_heuristic() # f(n) = h(n)
                    n.score += n.depth # f(n) = g(n) + h(n)

                    #print('nodo: ', n.depth,':', n.move, 'score: ', n.score)


                    self.elements.append(n)
                    self.elements_value.append(results[i])


                    for el in range(len(self.leaves)):


                        if el == self.leaves.index(self.leaves[-1]):  # se l'indice corrisponde con l'ultimo elemento
                            self.leaves.append(n)
                            #print('LO METTO IN CODA')
                            break


                        elif self.leaves[el].score > n.score:
                            self.leaves.insert(el, n)
                            break

                    if n.depth > self.max_depth:
                        self.max_depth = n.depth
                    if n.value == goal:
                        self.solution = 1
                        print('\n\t--- SOLUTION FOUND! ---\n', end='')
                        self.print_tree()
                        self.print_solution(n)
                        return None

            self.leaves.remove(self.leaves[0])




    def solve_bidirectional(self):
        self.expand_tree_BF(self.depth_limit)

        if (self.solution == 1): return None

        # create goal node
        goalNode = node(goal)
        goalNode.depth = 0
        goalNode.score = 0

        # create second search tree
        treeFromGoal = search_tree(root=goalNode, depth_limit=self.depth_limit)

        #start_time_goal = time.time()
        treeFromGoal.expand_tree_BF(self.depth_limit) # expand with bread-first the second tree

        #print tree and execution time
        treeFromGoal.print_tree()


        # find optimal solution
        for g in range(len(treeFromGoal.elements)):
            for s in range(len(self.elements)):
                if treeFromGoal.elements[g].value == self.elements[s].value:
                    print('\n\t--- SOLUTION FOUND! ---\n')

                    self.print_solution(self.elements[s])

                    treeFromGoal.print_solution_reverse(treeFromGoal.elements[g])

                    return None



start = 'GBOOYRWWGBWRGGRBRYOWY'
start2 = 'WWGGOOBWRRYGYGOWRRBYB'
start3 = 'WGGWBWRRYGOOYGOWRRBYB'
start5 = 'GRYWOGWGROBYBYBGWRWRO'
start6 = 'RROWGGWGYGOYRWBBRWBOY'
start7 = 'WRBOOGWYRBWGGGOBWRYYR'
start10 = 'RRORGWBGYGWYWOWRYGOBB'
start12 = 'GBOOYRWWGBWRGGRBRYOWY'




startNode = node(start5)
startNode.depth = 0
startNode.score = 0

#create search tree
treeFromRoot = search_tree(root=startNode, depth_limit=7)




start_time = time.time()

treeFromRoot.solve_bidirectional()

print('\n\nworked for ' + str(round(time.time() - start_time, 2)) + ' seconds')

