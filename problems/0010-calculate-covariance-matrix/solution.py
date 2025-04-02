def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
    m, n = len(vectors), len(vectors[0])
    ans_list = [[0.0] * m for i in range(m)]
    mean_i = [0] * len(vectors)
    for i in range(m):
        sum_i = 0
        for j in range(n):
            sum_i += vectors[i][j]
        mean_i[i] = sum_i * 1.0 / n
    for i in range(m):
        vectors[i] = [item - mean_i[i] for item in vectors[i]]
    for i in range(m):
        for j in range(m):
            ans_list[i][j] = sum(vectors[i][k] * vectors[j][k] for k in range(m)) / (m -1)
    return ans_list