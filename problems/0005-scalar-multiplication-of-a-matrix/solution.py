def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	m, n = len(matrix), len(matrix[0])
	res = [[0] * n for _ in range(m)]
	for i in range(m):
		for j in range(n):
			res[i][j] = matrix[i][j] * scalar
	return res