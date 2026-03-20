import numpy as np

def dot_product(v1, v2):
	return sum(v1[i]*v2[i] for i in range(len(v1)))


def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	return dot_product(v1, v2) / (np.sqrt(dot_product(v1, v1)) * np.sqrt(dot_product(v2, v2))) * 1.0
