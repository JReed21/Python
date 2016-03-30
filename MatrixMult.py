r = int(input("# of rows: "))
c = int(input("# of columns: "))
matrix1 = [[0]*c for i in range(r)]
print("Go in order from top left to bottom right, we are going to assume these matrixes can be multiplied: ")
col = len(matrix1[0])
for x in range(0,len(matrix1)):
	c = 0
	while(c < col):
		matrix1[x][c] = int(input("Row {0} column {1} ".format(x,c)))
		c += 1
print("Second matrix")
r = int(input("# of rows: "))
c = int(input("# of columns: "))
matrix2 = [[0]*c for i in range(r)]
print("Go in order from top left to bottom right, we are going to assume these matrixes can be multiplied: ")
col = len(matrix2[0])
for x in range(0,len(matrix2)):
	c = 0
	while(c < col):
		matrix2[x][c] = int(input("Row {0} column {1} ".format(x,c)))
		c += 1
NewMatrix = [[0]*len(matrix2[0]) for i in range(len(matrix1))]
col = len(matrix1[0])
summ = 0
for x in range(0,len(matrix1)):
	for y in range(0,len(matrix2[0])):
		c = 0
		while(c < col):
			summ += matrix1[x][c] * matrix2[c][y]
			c += 1
		NewMatrix[x][y] = summ
		summ = 0
print NewMatrix










