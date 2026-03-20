def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trace = matrix[0][0] + matrix[1][1]
	det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

	eig_max = (trace + (trace * trace - 4 * det) ** 0.5)/2
	eig_min = (trace - (trace * trace - 4 * det) ** 0.5)/2
	return [eig_max, eig_min]