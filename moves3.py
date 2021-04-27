# moves of 3x3x3 cube

def no_move(pos):
    return (pos[0] + pos[1] + pos[2] + pos[3] + pos[4] + pos[5] + pos[6] + pos[7] +
            pos[8] + pos[9] + pos[10] + pos[11] + pos[12] + pos[13] + pos[14] + pos[15] +
            pos[16] + pos[17] + pos[18] + pos[19] + pos[20] + pos[21] + pos[22] + pos[23] +
            pos[24] + pos[25] + pos[26] + pos[27] + pos[28] + pos[29] + pos[30] + pos[31] +
            pos[32] + pos[33] + pos[34] + pos[35] + pos[36] + pos[37] + pos[38] + pos[39] +
            pos[40] + pos[41] + pos[42] + pos[43] + pos[44] + pos[45] + pos[46] + pos[47])



def F(pos):
    return (pos[11] + pos[22] + pos[31] + pos[3] + pos[4] + pos[5] + pos[6] + pos[7] +
            pos[10] + pos[21] + pos[30] + pos[42] + pos[12] + pos[13] + pos[14] + pos[15] +
            pos[16] + pos[17] + pos[18] + pos[2] + pos[9] + pos[29] + pos[41] + pos[23] +
            pos[24] + pos[25] + pos[26] + pos[1] + pos[8] + pos[20] + pos[28] + pos[40] +
            pos[32] + pos[33] + pos[34] + pos[35] + pos[36] + pos[37] + pos[38] + pos[0] +
            pos[19] + pos[27] + pos[39] + pos[43] + pos[44] + pos[45] + pos[46] + pos[47])


def Fc(pos):
    return (pos[39] + pos[27] + pos[19] + pos[3] + pos[4] + pos[5] + pos[6] + pos[7] +
            pos[28] + pos[20] + pos[8] + pos[0] + pos[12] + pos[13] + pos[14] + pos[15] +
            pos[16] + pos[17] + pos[18] + pos[40] + pos[29] + pos[9] + pos[1] + pos[23] +
            pos[24] + pos[25] + pos[26] + pos[41] + pos[30] + pos[21] + pos[10] + pos[2] +
            pos[32] + pos[33] + pos[34] + pos[35] + pos[36] + pos[37] + pos[38] + pos[42] +
            pos[31] + pos[22] + pos[11] + pos[43] + pos[44] + pos[45] + pos[46] + pos[47])


def R(pos):
    return (pos[28] + pos[1] + pos[2] + pos[3] + pos[4] + pos[5] + pos[8] + pos[20] +
            pos[40] + pos[9] + pos[10] + pos[11] + pos[12] + pos[13] + pos[14] + pos[15] +
            pos[0] + pos[19] + pos[27] + pos[39] + pos[47] + pos[21] + pos[22] + pos[23] +
            pos[24] + pos[7] + pos[18] + pos[38] + pos[46] + pos[29] + pos[30] + pos[31] +
            pos[32] + pos[33] + pos[34] + pos[35] + pos[6] + pos[17] + pos[26] + pos[37] +
            pos[36] + pos[41] + pos[42] + pos[43] + pos[44] + pos[45] + pos[16] + pos[25])


def Rc(pos):
    return (pos[16] + pos[1] + pos[2] + pos[3] + pos[4] + pos[5] + pos[36] + pos[25] +
            pos[6] + pos[9] + pos[10] + pos[11] + pos[12] + pos[13] + pos[14] + pos[15] +
            pos[46] + pos[37] + pos[26] + pos[17] + pos[7] + pos[21] + pos[22] + pos[23] +
            pos[24] + pos[47] + pos[38] + pos[18] + pos[0] + pos[29] + pos[30] + pos[31] +
            pos[32] + pos[33] + pos[34] + pos[35] + pos[40] + pos[39] + pos[27] + pos[19] +
            pos[8] + pos[41] + pos[42] + pos[43] + pos[44] + pos[45] + pos[28] + pos[20])


def U(pos):
    return (pos[6] + pos[7] + pos[0] + pos[1] + pos[2] + pos[3] + pos[4] + pos[5] +
            pos[17] + pos[18] + pos[19] + pos[8] + pos[9] + pos[10] + pos[11] + pos[12] +
            pos[13] + pos[14] + pos[15] + pos[16] + pos[20] + pos[21] + pos[22] + pos[23] +
            pos[24] + pos[25] + pos[26] + pos[27] + pos[28] + pos[29] + pos[30] + pos[31] +
            pos[32] + pos[33] + pos[34] + pos[35] + pos[36] + pos[37] + pos[38] + pos[39] +
            pos[40] + pos[41] + pos[42] + pos[43] + pos[44] + pos[45] + pos[46] + pos[47])


def Uc(pos):
    return (pos[2] + pos[3] + pos[4] + pos[5] + pos[6] + pos[7] + pos[0] + pos[1] +
            pos[11] + pos[12] + pos[13] + pos[14] + pos[15] + pos[16] + pos[17] + pos[18] +
            pos[19] + pos[8] + pos[9] + pos[10] + pos[20] + pos[21] + pos[22] + pos[23] +
            pos[24] + pos[25] + pos[26] + pos[27] + pos[28] + pos[29] + pos[30] + pos[31] +
            pos[32] + pos[33] + pos[34] + pos[35] + pos[36] + pos[37] + pos[38] + pos[39] +
            pos[40] + pos[41] + pos[42] + pos[43] + pos[44] + pos[45] + pos[46] + pos[47])


def B(pos):
    return (pos[0] + pos[1] + pos[2] + pos[3] + pos[17] + pos[26] + pos[37] + pos[7] +
            pos[8] + pos[9] + pos[10] + pos[11] + pos[12] + pos[6] + pos[16] + pos[25] +
            pos[36] + pos[46] + pos[18] + pos[19] + pos[20] + pos[21] + pos[22] + pos[5] +
            pos[15] + pos[35] + pos[45] + pos[27] + pos[28] + pos[29] + pos[30] + pos[31] +
            pos[32] + pos[4] + pos[14] + pos[24] + pos[34] + pos[44] + pos[38] + pos[39] +
            pos[40] + pos[41] + pos[42] + pos[43] + pos[13] + pos[23] + pos[33] + pos[47])


def Bc(pos):
    return (pos[0] + pos[1] + pos[2] + pos[3] + pos[33] + pos[23] + pos[13] + pos[7] +
            pos[8] + pos[9] + pos[10] + pos[11] + pos[12] + pos[44] + pos[34] + pos[24] +
            pos[14] + pos[4] + pos[18] + pos[19] + pos[20] + pos[21] + pos[22] + pos[45] +
            pos[35] + pos[15] + pos[5] + pos[27] + pos[28] + pos[29] + pos[30] + pos[31] +
            pos[32] + pos[46] + pos[36] + pos[25] + pos[16] + pos[6] + pos[38] + pos[39] +
            pos[40] + pos[41] + pos[42] + pos[43] + pos[37] + pos[26] + pos[17] + pos[47])


def L(pos):
    return (pos[0] + pos[1] + pos[14] + pos[24] + pos[34] + pos[5] + pos[6] + pos[7] +
            pos[8] + pos[9] + pos[4] + pos[13] + pos[23] + pos[33] + pos[44] + pos[15] +
            pos[16] + pos[17] + pos[18] + pos[19] + pos[20] + pos[3] + pos[12] + pos[32] +
            pos[43] + pos[25] + pos[26] + pos[27] + pos[28] + pos[29] + pos[2] + pos[11] +
            pos[22] + pos[31] + pos[42] + pos[35] + pos[36] + pos[37] + pos[38] + pos[39] +
            pos[40] + pos[41] + pos[10] + pos[21] + pos[30] + pos[45] + pos[46] + pos[47])

def Lc(pos):
    return (pos[0] + pos[1] + pos[30] + pos[21] + pos[10] + pos[5] + pos[6] + pos[7] +
            pos[8] + pos[9] + pos[42] + pos[31] + pos[22] + pos[11] + pos[2] + pos[15] +
            pos[16] + pos[17] + pos[18] + pos[19] + pos[20] + pos[43] + pos[32] + pos[12] +
            pos[3] + pos[25] + pos[26] + pos[27] + pos[28] + pos[29] + pos[44] + pos[33] +
            pos[23] + pos[13] + pos[4] + pos[35] + pos[36] + pos[37] + pos[38] + pos[39] +
            pos[40] + pos[41] + pos[34] + pos[24] + pos[14] + pos[45] + pos[46] + pos[47])


def D(pos):
    return (pos[0] + pos[1] + pos[2] + pos[3] + pos[4] + pos[5] + pos[6] + pos[7] +
            pos[8] + pos[9] + pos[10] + pos[11] + pos[12] + pos[13] + pos[14] + pos[15] +
            pos[16] + pos[17] + pos[18] + pos[19] + pos[20] + pos[21] + pos[22] + pos[23] +
            pos[24] + pos[25] + pos[26] + pos[27] +  pos[31] + pos[32] + pos[33] + pos[34] +
            pos[35] + pos[36] + pos[37] + pos[38] + pos[39] + pos[28] + pos[29] + pos[30] +
            pos[42] + pos[43] + pos[44] + pos[45] + pos[46] + pos[47] + pos[40] + pos[41] )

def Dc(pos):
    return (pos[0] + pos[1] + pos[2] + pos[3] + pos[4] + pos[5] + pos[6] + pos[7] +
            pos[8] + pos[9] + pos[10] + pos[11] + pos[12] + pos[13] + pos[14] + pos[15] +
            pos[16] + pos[17] + pos[18] + pos[19] + pos[20] + pos[21] + pos[22] + pos[23] +
            pos[24] + pos[25] + pos[26] + pos[27] + pos[37] + pos[38] + pos[39] + pos[28] +
            pos[29] + pos[30] + pos[31] + pos[32] + pos[33] + pos[34] + pos[35] + pos[36] +
            pos[46] + pos[47] + pos[40] + pos[41] + pos[42] + pos[43] + pos[44] + pos[45] )
