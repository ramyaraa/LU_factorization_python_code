
# create a varable A and assign a list of lists to it matrix 10 by 10
A = [[1, 2, 3, 4, 5,1],]

# loop through the list of lists and check if row > column make it 0
# for i in range(0,4):
#     for j in range(0,4):
#         if i > j:
#             A[i][j] = 0

for row in range(0, len(A)):
    for column in range(0, len(A)):
        if row > column:
            A[row][column] = 0


for row in A:
    print(row)