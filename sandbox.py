from itertools import permutations
from scipy.spatial.distance import cdist
import numpy as np

solved = np.array([[1,1,1],[0,1,1],[0,1,0],[1,1,0],[1,0,1],[0,0,1],[1,0,0]]) #noto
#---------------------0-------1-------2-------3-------4-------5-------6-----------



#print(solved)
#print(solved[0])

goal = 'WWWWGGOOBBRRGGOBRRYYY'
start = 'WYBOROGWOWGBGRWBRRYGY'
start2 = 'WWGGOOBWRRYGYGOWRRBYB'
start3 = 'WGGWBWRRYGOOYGOWRRBYB'
start5 = 'GRYWOGWGROBYBYBGWRWRO'
start6 = 'RROWGGWGYGOYRWBBRWBOY'


def compute_heuristic(string):

    cubelets = [string[0] + string[4] + string[11],
                string[1] + string[5] + string[6],
                string[2] + string[7] + string[8],
                string[3] + string[9] + string[10],
                string[12] + string[17] + string[18],
                string[13] + string[14] + string[19],
                string[15] + string[16] + string[20]]

    positions = np.empty((0,3))
    #print(positions)
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

    return sum(  np.diag(  cdist(  solved, positions, metric='cityblock'  )  )  )



print(compute_heuristic(start6))




