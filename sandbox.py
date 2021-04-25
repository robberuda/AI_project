from itertools import permutations
from scipy.spatial.distance import cdist

A = (0,0,0)
B = (1,0,1)
out = cdist(A, B, metric='cityblock')
print(out)


goal = 'WWWWGGOOBBRRGGOBRRYYY'
start = 'WYBOROGWOWGBGRWBRRYGY'
start2 = 'WWGGOOBWRRYGYGOWRRBYB'
start3 = 'WGGWBWRRYGOOYGOWRRBYB'
start5 = 'GRYWOGWGROBYBYBGWRWRO'
start6 = 'RROWGGWGYGOYRWBBRWBOY'


def find_position(string):

    cubelets = [string[0] + string[4] + string[11],
                string[1] + string[5] + string[6],
                string[2] + string[7] + string[8],
                string[3] + string[9] + string[10],
                string[12] + string[17] + string[18],
                string[13] + string[14] + string[19],
                string[15] + string[16] + string[20]]
    positions = []
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
        positions.append(id)
    return positions


positions = find_position(start)
print(positions)

#[3, 5, 2, 1, 4, 0, 6]

#[0, 1, 2, 3, 4, 5, 6]




