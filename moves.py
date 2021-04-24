# Hard coded moves to perform on the cube.
# Position is passed in and returned with the stickers in the order they should be after the turn.


# Hard coded moves to perform on the cube.
# Position is passed in and returned with the stickers in the order they should be after the turn.

# Front Quarter Turn Clockwise
def F(pos):
	return (pos[6] + pos[14] + pos[2] +
			pos[3] + pos[5] + pos[13] +
			pos[19] + pos[7] + pos[8] +
			pos[9] + pos[10] + pos[1] +
			pos[4] + pos[12] + pos[18] +
			pos[15] + pos[16] + pos[0] +
			pos[11] + pos[17] + pos[20])

# Front Quarter Turn Counterclockwise
def Fc(pos):
	return (pos[17] + pos[11] + pos[2] +
			pos[3] + pos[12] + pos[4] +
			pos[0] + pos[7] + pos[8] +
			pos[9] + pos[10] + pos[18] +
			pos[13] + pos[5] + pos[1] +
			pos[15] + pos[16] + pos[19] +
			pos[14] + pos[6] + pos[20])


# Right Quarter Turn Clockwise
def R(pos):
	return (pos[12] + pos[1] + pos[2] +
			pos[4] + pos[18] + pos[5] +
			pos[6] + pos[7] + pos[8] +
			pos[0] + pos[11] + pos[17] +
			pos[20] + pos[13] + pos[14] +
			pos[3] + pos[10] + pos[16] +
			pos[15] + pos[19] + pos[9])

# Right Quarter Turn Counterclockwise
def Rc(pos):
	return (pos[9] + pos[1] + pos[2] +
			pos[15] + pos[3] + pos[5] +
			pos[6] + pos[7] + pos[8] +
			pos[20] + pos[16] + pos[10] +
			pos[0] + pos[13] + pos[14] +
			pos[18] + pos[17] + pos[11] +
			pos[4] + pos[19] + pos[12])

# Up Quarter Turn Clockwise
def U(pos):
	return (pos[3] + pos[0] + pos[1] +
			pos[2] + pos[10] + pos[11] +
			pos[4] + pos[5] + pos[6] +
			pos[7] + pos[8] + pos[9] +
			pos[12] + pos[13] + pos[14] +
			pos[15] + pos[16] + pos[17] +
			pos[18] + pos[19] + pos[20])

# Up Quarter Turn Counterclockwise
def Uc(pos):
	return (pos[1] + pos[2] + pos[3] +
			pos[0] + pos[6] + pos[7] +
			pos[8] + pos[9] + pos[10] +
			pos[11] + pos[4] + pos[5] +
			pos[12] + pos[13] + pos[14] +
			pos[15] + pos[16] + pos[17] +
			pos[18] + pos[19] + pos[20])
