import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'column':
		axis = 0
	else:
		axis = 1
	return np.mean(matrix, axis = axis)
