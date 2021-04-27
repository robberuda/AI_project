#main cube 3x3x3 solver

import moves3
import time
from scipy.spatial.distance import cdist
import numpy as np

## è ancoraa solo una copia di main3.py,

##---------------WORK IN PROGRESS



# definition of node ---------------------------------------------------------------------------------------------------
class node:
    def __init__(self, value=None, move=None, parent=None, depth=0):
        self.value = value
        self.move = move
        self.parent = parent  # pointer to parent node in tree
        self.depth = depth
        #self.score = None # ancora non usata



# definition of search tree --------------------------------------------------------------------------------------------
class search_tree:
    def __init__(self, root = None, depth_limit=3):
        self.root = root
        self.elements = [root]
        self.elements_value = [root.value]
        self.leaves = [root]
        self.max_depth = 0
        self.solution = 0
        self.depth_limit = depth_limit + 1
        self.goal = 'WWWWWWWWGGGOOOBBBRRRGGOOBBRRGGGOOOBBBRRRYYYYYYYY'

    def print_solution(self,n):
        sol = []
        print('solution is :', end='')
        for d in range(n.depth):
            sol.append(n.move)
            n = n.parent
        sol.reverse()
        print(sol,end='')

    def print_level(self, level):
        print('level', level, ':', end=' ')
        father_move = 'N'
        for el in self.elements:
            if el.depth == level :
                if (level != 0):print(el.parent.move, end='->')
                print(el.move, end=' ')
        print('\n')

    def print_tree(self):
        print('max depth is: ', self.max_depth)
        for i in range(self.max_depth+1):
            cnt=0
            for el in self.elements:
                if el.depth == i:
                    cnt +=1
            print(i,': ', cnt)


    def expand_tree_BF(self, depth=3):

        self.depth_limit = depth

        while self.max_depth < self.depth_limit:

            results = [moves3.F(self.leaves[0].value), moves3.Fc(self.leaves[0].value),
                       moves3.R(self.leaves[0].value), moves3.Rc(self.leaves[0].value),
                       moves3.U(self.leaves[0].value), moves3.Uc(self.leaves[0].value),
                       moves3.B(self.leaves[0].value), moves3.Bc(self.leaves[0].value),
                       moves3.L(self.leaves[0].value), moves3.Lc(self.leaves[0].value),
                       moves3.D(self.leaves[0].value), moves3.Dc(self.leaves[0].value) ]

            for i in range(len(results)):

                if results[i] not in self.elements_value:
                    n = node(results[i])
                    n.move = moves3.moves_index[i]
                    n.parent = self.leaves[0]
                    n.depth = self.leaves[0].depth + 1

                    self.elements.append(n)
                    self.elements_value.append(results[i])
                    self.leaves.append(n)

                    if n.depth > self.max_depth:
                        self.max_depth = n.depth

                    if n.value == self.goal:
                        self.solution = 1
                        print('\n\n\n\nSOLUTION FOUND: ', end='')
                        self.print_tree()
                        self.print_solution(n)
                        return None
                        #break

            self.leaves.remove(self.leaves[0])



    #def solve(self):
        # trova la soluzione per completare una faccia

        # trova la soluzione per completare lo strato sopra il livello appena fatto

        #self.goal = 'WWWWWWWWGGGOOOBBBRRRGGOOBBRRGGGOOOBBBRRRYYYYYYYY'



#-----------------------------------------------------------------------------main:

goalNode = node(value='WWWWWWWWGGGOOOBBBRRRGGOOBBRRGGGOOOBBBRRRYYYYYYYY', move='goal')
start3   = node(value='OGGWWWWWWRRYGGOOBRRBWGOOBBRBGGGOOOBBBRRWRYYYYYYY', move='root')
start4   = node(value='WWGGGGRWBBWRRYOOYGOOYYOGWWRRYGYOOGWBWRRRBYBBOYBB', move='root')
start5   = node(value='BWWWOGGBYBBRRBWRRYOOYWOOYWGROOOYBWGRRYGWGGGYRBBY', move='root')

tree = search_tree(root=start5)




start_time = time.time()

tree.expand_tree_BF(depth = 6)
if(tree.solution == 0): tree.print_tree()

print('\nworked for ' + str(round(time.time() - start_time, 2)) + ' seconds')