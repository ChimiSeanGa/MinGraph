import sys

def getMatrix():
	dim = int(raw_input())
	mat = []

	for col in range(dim):
		row = [int(x) for x in raw_input().split()]
		if len(row) != dim:
			print('Invalid row')
			return
		mat.append(row)

	return mat

def getWeights():
	return [float(x) for x in raw_input().split()]

def calcScore(matrix, weights):
	distSum = 0
	for i in range(len(matrix)):
		for j in range(i, len(matrix)):
			if matrix[i][j] == 1:
				distSum += (weights[i] - weights[j])**2

	weightSum = 0.0
	for i in range(len(weights)):
		weightSum += weights[i]**2

	return distSum / weightSum

def main():
	matrix = getMatrix()
	weights = getWeights()
	score = calcScore(matrix, weights)
	print('Your score is ' + str(score))

if __name__ == '__main__':
	main()
