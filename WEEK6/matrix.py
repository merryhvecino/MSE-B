import numpy as np

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = np.array(matrix)
print(res)



matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = np.array(matrix).flatten()
print(res)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = numpy.array(matrix).reshape(-1)
print(res)
