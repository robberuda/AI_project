# Hard coded moves to perform on the cube.
# Position is passed in and returned with the stickers in the order they should be after the turn.

# Up Quarter Turn Clockwise
def noMove(pos):
	return (pos[0]  + pos[1] +
	        pos[2]  + pos[3] +
	        pos[4]  + pos[5]  + pos[6]  + pos[7]  + pos[8]  + pos[9]  + pos[10] + pos[11] +
	        pos[12] + pos[13] + pos[14] + pos[15] + pos[16] + pos[17] + pos[18] + pos[19] +
			pos[20] + pos[21] +
			pos[22] + pos[23])


# Up Quarter Turn Clockwise
def U(pos):
	return (pos[2]  + pos[0] +
			pos[3]  + pos[1] +
			pos[6]  + pos[7] + pos[8] + pos[9] + pos[10] + pos[11] + pos[4] + pos[5] +
			pos[12] + pos[13] + pos[14] + pos[15] + pos[16] + pos[17] + pos[18] + pos[19] +
			pos[20] + pos[21] +
			pos[22] + pos[23])

# Right Quarter Turn Clockwise
def R(pos):
	return (pos[0]  + pos[5]  +
			pos[2]  + pos[13] +
			pos[4]  + pos[21] + pos[14] + pos[6] + pos[3]  + pos[9]  + pos[10] + pos[11] +
			pos[12] + pos[23] + pos[15] + pos[7] + pos[1]  + pos[17] + pos[18] + pos[19] +
			pos[20] + pos[16] +
			pos[22] + pos[8])

# Left Quarter Turn Clockwise
def L(pos):
	return (pos[17] + pos[1] +
	        pos[9] + pos[3] +
	        pos[0]  + pos[5]  + pos[6]  + pos[7]  + pos[8]  + pos[22]  + pos[18] + pos[10] +
	        pos[2]  + pos[13] + pos[14] + pos[15] + pos[16] + pos[20] + pos[19] + pos[11] +
			pos[4]  + pos[21] +
			pos[12] + pos[23])

# Down Quarter Turn Clockwise
def D(pos):
	return (pos[0]  + pos[1] +
	        pos[2]  + pos[3] +
	        pos[4]  + pos[5]  + pos[6]  + pos[7]  + pos[8]  + pos[9]  + pos[10] + pos[11] +
	        pos[18] + pos[19] + pos[12] + pos[13] + pos[14] + pos[15] + pos[16] + pos[17] +
			pos[22] + pos[20] +
			pos[23] + pos[21])

# Front Quarter Turn Clockwise
def F(pos):
	return (pos[0]  + pos[1] +
	        pos[19] + pos[11] +
	        pos[12] + pos[4] + pos[2]  + pos[7]  + pos[8]  + pos[9]  + pos[10] + pos[20] +
	        pos[13] + pos[5] + pos[3] + pos[15] + pos[16] + pos[17] + pos[18] + pos[21] +
			pos[15] + pos[14] +
			pos[22] + pos[23])

# Back Quarter Turn Clockwise
def B(pos):
	return (pos[7]  + pos[15] +
	        pos[2]  + pos[3] +
	        pos[4]  + pos[5]  + pos[6]  + pos[23] + pos[16] + pos[8]  + pos[1] + pos[11] +
	        pos[12] + pos[13] + pos[14] + pos[22] + pos[17] + pos[9] + pos[0] + pos[19] +
			pos[20] + pos[21] +
			pos[10] + pos[18])