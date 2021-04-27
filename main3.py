#main cube 3x3x3 solver

import moves3
import time
from scipy.spatial.distance import cdist
import numpy as np

goal = 'WWWWWWWWGGGOOOBBBRRRGGOOBBRRGGGOOOBBBRRRYYYYYYYY'

moves_index = {0:'F', 1:'Fc', 2:'R', 3:'Rc', 4:'U', 5:'Uc', 6:'B', 7:'Bc', 8:'L', 9:'Lc', 10:'D', 11:'Dc'}

# definition of node ---------------------------------------------------------------------------------------------------
class node:

    def __init__(self, value=None, move=None, parent=None):
        self.value = value
        self.move = move
        self.parent = parent  # pointer to parent node in tree
        self.depth = None
        self.score = None