# Write a Python Program to Multiply Two Matrices
def matrix_multiply(matrix1, matrix2):
    # Check if the matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        print("Matrices cannot be multiplied. Number of columns in the first matrix should be equal to the number of rows in the second matrix.")
        return None

    # Create a result matrix filled with zeros
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    # Perform matrix multiplication
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result
    
if __name__ == '__main__':
    matrix_a = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]

    matrix_b = [[9, 8, 7],
                [6, 5, 4],
                [3, 2, 1]]

    result_matrix = matrix_multiply(matrix_a, matrix_b)

    if result_matrix:
        print("Result of matrix multiplication:")
        for row in result_matrix:
            print(row)
