# Math❌-Meth✔️
## Matrix Operations with Checkmarks and Crosses

This project includes Python code for performing basic matrix operations using NumPy. Users can input the elements of matrices of any size from the keyboard. The script also provides checkmarks (✔️) and crosses (❌) to indicate whether certain conditions are met (e.g., if a matrix is invertible).

## Operations Included

1. Creation of a matrix via user input
2. Calculation of the determinant of a square matrix
3. Calculation of the inverse of a square matrix (if it exists)
4. Multiplication of two matrices

## How to Use

1. Clone the repository:
     git clone https://github.com/Chinilshik-kalkulatorov/Math-Meth-.git
   
2. Navigate to the project directory:
     cd Math-Meth-
   
3. Run the Python script:
     python matrix_operations.py
   
4. Follow the prompts to input the size and elements of the matrices. Enter each row of the matrix as space-separated numbers.

## Example

After running the script, you will be prompted to enter the size and elements of two matrices. The script will then display the determinant of the first matrix (if it is square), its inverse (if it is square and invertible), and the product of the two matrices, along with checkmarks and crosses to indicate certain conditions.

### Sample Input
Enter the number of rows for Matrix 1: 2
Enter the number of columns for Matrix 1: 3
Enter the elements of the 2x3 matrix row by row, separating numbers with spaces:
1 2 3
4 5 6

Enter the number of rows for Matrix 2: 3
Enter the number of columns for Matrix 2: 2
Enter the elements of the 3x2 matrix row by row, separating numbers with spaces:
7 8
9 10
11 12

### Sample Output
Matrix 1:
[[1. 2. 3.]
 [4. 5. 6.]]

Matrix 2:
[[ 7.  8.]
 [ 9. 10.]
 [11. 12.]]

Matrix 1 is not square, so the determinant is not defined. ❌

Matrix 1 is not square, so the inverse is not defined. ❌

Product of Matrix 1 and Matrix 2:
[[ 58.  64.]
 [139. 154.]]

## Dependencies

- Python 3.x
- NumPy

Install the dependencies using pip:pip install numpy

## License

This project is licensed under the MIT License.
