import moves2
import time

solvedCube = 'WWWWGGOOBBRRGGOBRRYYY'
# Solves the problem
def solve():
	start_time = time.time()
	dist = [{solvedCube}, set(moves2.get_moves(solvedCube))]
	while dist[-1]:
		dist.append(set())
		for pos in dist[-2]:
			for sub_pos in moves2.get_moves(pos):
				if sub_pos not in dist[-2] and sub_pos not in dist[-3]:
					dist[-1].add(sub_pos)
					if len(dist)-1 == 0:
						print(len(dist), ': ', sub_pos)
		print('Depth ' + str(len(dist) - 1) + ': ' + str(len(dist[-1])) + ' positions')
	print('2x2 Depth is ' + str(len(dist) - 2) + ', solved in ' + str(round(time.time() - start_time, 2)) + ' seconds')

solve()