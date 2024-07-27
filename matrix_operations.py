import numpy as np

def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements of the {rows}x{cols} matrix row by row, separating numbers with spaces:")
    for _ in range(rows):
        row = list(map(float, input().split()))
        if len(row) != cols:
            print(f"Error: Please enter exactly {cols} numbers.")
            return None
        matrix.append(row)
    return np.array(matrix)

def main():
    rows1 = int(input("Enter the number of rows for Matrix 1: "))
    cols1 = int(input("Enter the number of columns for Matrix 1: "))
    matrix1 = input_matrix(rows1, cols1)
    if matrix1 is None:
        return
    print(matrix1)

    rows2 = int(input("\nEnter the number of rows for Matrix 2: "))
    cols2 = int(input("Enter the number of columns for Matrix 2: "))
    if cols1 != rows2:
        print("Error: The number of columns of Matrix 1 must equal the number of rows of Matrix 2 for multiplication.")
        return
    matrix2 = input_matrix(rows2, cols2)
    if matrix2 is None:
        return
    print(matrix2)

    # Calculate the determinant of the first matrix (only if it's square)
    if rows1 == cols1:
        det_matrix1 = np.linalg.det(matrix1)
        print(f"\nDeterminant of Matrix 1: {det_matrix1}")
        print_check_or_cross(det_matrix1 != 0)
    else:
        print("\nMatrix 1 is not square, so the determinant is not defined.")
        print_check_or_cross(False)

    # Find the inverse of the first matrix (only if it's square and invertible)
    if rows1 == cols1:
        try:
            inv_matrix1 = np.linalg.inv(matrix1)
            print("\nInverse of Matrix 1:")
            print(inv_matrix1)
            print_check_or_cross(True)
        except np.linalg.LinAlgError:
            print("\nMatrix 1 does not have an inverse matrix")
            print_check_or_cross(False)
    else:
        print("\nMatrix 1 is not square, so the inverse is not defined.")
        print_check_or_cross(False)

    # Multiply the two matrices
    product_matrix = np.dot(matrix1, matrix2)
    print("\nProduct of Matrix 1 and Matrix 2:")
    print(product_matrix)

def print_check_or_cross(condition):
    if condition:
        print("✔️")
    else:
        print("❌")

if name == "__main__":
    main()
