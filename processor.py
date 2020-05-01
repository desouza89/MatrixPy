import sys

matrix_C = []
matrix_A = []
matrix_B = []


def add_matrix():
    n1 = input("Enter size of first matrix:")  # Defining matrix A
    row_lines = [int(x) for x in n1.split()]
    print("Enter first matrix:")
    for i in range(row_lines[0]):
        i = input()
        np = [float(x) for x in i.split()]
        matrix_A.append(np)

    n2 = input("Enter size of second matrix:")  # Defining matrix B
    row_lines_1 = [int(x) for x in n2.split()]

    if row_lines != row_lines_1:  # Checking if operation is possible
        print("The operation cannot be performed.\n")
        start()

    print("Enter second matrix:")
    for i in range(row_lines_1[0]):
        i = input()
        np = [float(x) for x in i.split()]
        matrix_B.append(np)

    length = len(matrix_A)
    height = len(matrix_A[0])

    for i in range(length):
        matrix_C.append([])
        for j in range(height):
            matrix_C[i].append(matrix_A[i][j] + matrix_B[i][j])

    print("The result is:")
    for i in range(len(matrix_C)):
        print(' '.join(map(str, matrix_C[i])))
    print()


def matrix_const():
    n1 = input("Enter size of matrix:")  # Defining matrix
    row_lines = [int(x) for x in n1.split()]
    print("Enter first matrix:")
    for i in range(row_lines[0]):
        i = input()
        np = [float(x) for x in i.split()]
        matrix_A.append(np)

    print("Enter constant:")
    const_ = float(input())  # Defining constant

    for i in range(len(matrix_A)):
        matrix_C.append([])
        for j in range(len(matrix_A[0])):
            matrix_C[i].append(const_ * matrix_A[i][j])

    for i in range(len(matrix_C)):
        print(' '.join(map(str, matrix_C[i])))


def matrix_product(a, b, len_a, len_b):
    length = len_a[0]  # Number of rows of Matrix A
    height = len_b[1]  # Number of columns of Matrix_B

    c = [[0] * height for i in range(length)]  # Filling matrix C with 0 elements

    for rows in range(length):
        for columns in range(height):
            for k in range(len_b[0]):
                c[rows][columns] += a[rows][k] * b[k][columns]
    return c


def start():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("0. Exit")
    user_choice = int(input("Your choice:"))

    if user_choice == 1:
        add_matrix()
        start()
    elif user_choice == 2:
        matrix_const()
        start()
    elif user_choice == 3:
        matrix_A.clear()
        n1 = input("Enter size of first matrix:")  # Defining matrix A
        row_lines = [int(x) for x in n1.split()]
        print("Enter first matrix:")
        for i in range(row_lines[0]):
            i = input()
            np = [float(x) for x in i.split()]
            matrix_A.append(np)

        n2 = input("Enter size of second matrix:")  # Defining matrix B
        row_lines_1 = [int(x) for x in n2.split()]

        if row_lines[1] != row_lines_1[0]:  # Check Columns of Matrix_A are equal to Rows of Matrix_B
            print("The operation cannot be performed.\n")
            start()

        print("Enter second matrix:")
        matrix_B.clear()
        for i in range(row_lines_1[0]):
            i = input()
            np = [float(x) for x in i.split()]
            matrix_B.append(np)

        NewOne = matrix_product(matrix_A, matrix_B, row_lines, row_lines_1)

        print("The result is:")
        for i in range(len(NewOne)):
            print(' '.join(map(str, NewOne[i])))
        print()
        start()
    elif user_choice == 0:
        sys.exit(1)


start()
