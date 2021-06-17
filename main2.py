import moves2
import time

# definition of node ---------------------------------------------------------------------------------------------------
class node:

    def __init__(self, value=None, move=None, parent=None):
        self.value = value    # value of the node, is the string that represent its configuration
        self.move = move      # move used to arrive at this node
        self.parent = parent  # pointer to the parent node
        self.depth = 0        # depth of the node


# definition of search tree --------------------------------------------------------------------------------------------
class search_tree:

    def __init__(self, root = None):
        self.root = root                        # root of tree, is a class node that contain start value
        self.elements = [self.root]             # elements contain all node of the tree
        self.elements_value = [self.root.value] # elements_value contain only the strings of element of the tree
        self.leaves = [self.root]               # leaves contain all node of the tree that not have child
        self.solutionNode = None                # solutionNode is a class node, it is the goal node that is the solution of the tree


    def print_trees_bidirectional(self, goaltree):
        for i in range(self.solutionNode.depth+1):
            cnt = 0
            for el in self.elements:
                if el.depth == i:
                    cnt += 1
            if i==0: print(i, ': ', cnt, "  --->  start node:", self.root.value)
            else:    print(i, ': ', cnt)
        print('=== Find equivalence in two trees ===')
        for i in reversed(range(goaltree.solutionNode.depth+1)):
            cnt = 0
            for el in goaltree.elements:
                if el.depth == i:
                    cnt += 1
            if i==0: print(i, ': ', cnt, "  --->  goal node:", goal)
            else:    print(i, ': ', cnt)


    def print_solution_bidirectional(self,nod, nod2):
        sol = []
        print('\n --- solution is:   ', end='')
        for d in range(nod.depth):
            sol.append(nod.move)
            nod = nod.parent
        sol.reverse()
        for s in range(len(sol)):
            if s!=0:
                print(' -> ', end='')
            print(sol[s], end='')
        for d in range(nod2.depth):
            print(' -> ',moves2.moves_index_reverse[nod2.move], end='')
            nod2 = nod2.parent
        print('   --- ')


    def solve_bidirectional(self):
        # if the root node is the goal configuration exit and report the situation:
        if self.root.value == goal:
            print('\n\t--- SOLUTION FOUND! ---\n')
            print('\n\t--- root is already the solution, solved in 0 moves ---\n')
            return None

        # create goal node for the second tree
        goalNode = node(goal)
        goalNode.depth = 0
        goalNode.score = 0

        # create second search tree with goal node as root
        treeFromGoal = search_tree(root=goalNode)


        while 1:
            # from here the the expantion of the main tree -------------------------------------------------------------
            results = moves2.get_moves(self.leaves[0].value)

            for i in range(len(results)):
                if results[i] not in self.elements_value:
                    n = node(results[i])
                    n.move = moves2.moves_index[i]
                    n.parent = self.leaves[0]
                    n.depth = self.leaves[0].depth + 1
                    self.elements.append(n)
                    self.elements_value.append(results[i])
                    self.leaves.append(n)

                    # compare the new node with all leaves node of second tree with goal node as root
                    # so the first time compare only with the goal node
                    for j in treeFromGoal.leaves:
                        if n.value == j.value:
                            print('\n\t--- SOLUTION FOUND! ---\n')
                            print('\t--- solvable in', (n.depth+ j.depth), 'moves---\n')
                            self.solutionNode = n

                            treeFromGoal.solution = 1
                            treeFromGoal.solutionNode = j

                            self.print_trees_bidirectional(goaltree=treeFromGoal)
                            self.print_solution_bidirectional(self.solutionNode, treeFromGoal.solutionNode)
                            return 0
            self.leaves.remove(self.leaves[0])

            # from here the the expantion of the second tree, from goal state ------------------------------------------
            results2 = moves2.get_moves(treeFromGoal.leaves[0].value)

            for i in range(len(results)):
                if results2[i] not in treeFromGoal.elements_value:
                    n = node(results2[i])
                    n.move = moves2.moves_index[i]
                    n.parent = treeFromGoal.leaves[0]
                    n.depth = treeFromGoal.leaves[0].depth + 1
                    treeFromGoal.elements.append(n)
                    treeFromGoal.elements_value.append(results2[i])
                    treeFromGoal.leaves.append(n)

                    # compare the new node with all leaves node of second tree with goal node as root
                    # so the first time compare only with the goal node
                    for j in self.leaves:
                        if n.value == j.value:
                            print('\n\t--- SOLUTION FOUND! ---\n')
                            print('\t--- solvable in', (n.depth+ j.depth), 'moves---\n')
                            treeFromGoal.solution = 1
                            treeFromGoal.solutionNode = n

                            self.solutionNode = j

                            self.print_trees_bidirectional(goaltree=treeFromGoal)
                            self.print_solution_bidirectional(self.solutionNode, treeFromGoal.solutionNode)
                            return 0

            treeFromGoal.leaves.remove(treeFromGoal.leaves[0])



# Main procedure:

solvedCube = 'WWWWGGOOBBRRGGOBRRYYY'  # string that represent an ordered cube

# Multiple cases to tests algorithm, from 2 moves to solve to 14 moves to solve (worst case):
start2 = 'WWBBOOBYRRWGWGOYRRGYG'
start3 = 'WWBOGGOYRBWRWGOYRBRYG'
start4 = 'GBOGYRWGYWRRYWOWBRBGO'
start5 = 'YWRYROBGWRBGYOGRBOGWW'
start6 = 'YROOBGWGYBWRYRBWOGRWG'
start7 = 'GWBRYOBRWGWRGGWBRYOOY'
start8 = 'OOWBGGYOBRWWBGYRWYRRG'
start9 = 'OBGWWYRWRBRBYOGOYGRWG'
start10= 'GWOYYOBWGRBRWYGGRBROW'
start11= 'RWGYWOBYORBGWBWGYGORR'
start12= 'GYBWOGRRWRGYWBOYBGOWR'
start13= 'RRGYYWBWRGRBGOWOYOWBG'
start14= 'YYWBROGOBYRGGGRWROWWB'

startRandom = 'WYOBGGRGYYRRORBOWWGWB' # ## you can change this string if you want to use another start condition ## #


start = startRandom # ## START CONDITION, CHANGE WITH A STRING ABOVE     ## #-------------------------------------------
goal  = solvedCube  # ## GOAL CONDITION, NOT NECESSARILY THE SOLVED CUBE ## #-------------------------------------------


startNode = node(start5)

treeFromRoot = search_tree(root=startNode) # create main search tree

start_time = time.time()
treeFromRoot.solve_bidirectional() # find the solution using bidirectional search
print('\t\n --- Solution found in ' + str(round(time.time() - start_time, 2)) + ' seconds ---\n')