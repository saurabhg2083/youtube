# Write a Python Program to Transpose a Matrix.
def transpose_matrix(matrix):
    # Get the dimensions of the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix to store the transposed values
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    # Iterate through the matrix and transpose the elements
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed
    
if __name__ == '__main__':
    matrix = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    transposed_matrix = transpose_matrix(matrix)

    print("Original Matrix:")
    for row in matrix:
        print(row)

    print("\nTransposed Matrix:")
    for row in transposed_matrix:
        print(row)
