def input_matrix(rows,cols,name="matrix"):
    matrix=[]
    print(f"enter element {rows}x{cols}matrix:")
    for i in range(rows):
        row=[]
        for j in range(cols):
            val=int(input(f" enter elements [{i}][{j}]: "))
            row.append(val)
        matrix.append(row)
    return matrix

def add_matrix(A,B):
    result=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j]+B[i][j])
        result.append(row)
    return result


def sub_matrix(A,B):
     result=[]
     for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        result.append(row)
     return result


def multi_matrix(A,B):
    result=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(B[0])):
            s=0
            for k in range(len(B)):
                s +=A[i][k]*B[k][j]
            row.append(s)
        result.append(row)
    return result

    
def determinant_3x3(M):
    return (M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1])
          - M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0])
          + M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0]))          
def cofactor_matrix(M):
    cof = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            minor = [[M[x][y] for y in range(3) if y != j] 
                     for x in range(3) if x != i]
            cof[i][j] = ((-1)**(i+j)) * (minor[0][0]*minor[1][1]-minor[0][1]*minor[1][0])
    return cof
def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
def inverse_matrix(M):
    det = determinant_3x3(M)
    if det == 0:
        raise ValueError("Matrix is not invertible")
    cof = cofactor_matrix(M)
    adj = transpose(cof)
    return [[adj[i][j]/det for j in range(3)] for i in range(3)]
def multiply_matrix(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            s = 0
            for k in range(len(B)):
                s += A[i][k] * B[k][j]
            row.append(s)
        result.append(row)
    return result

A = input_matrix(3, 3, "Matrix A")
B = input_matrix(3, 3, "Matrix B")
B_inv = inverse_matrix(B)
result = multiply_matrix(A, B_inv)

print("Inverse of B:")
for row in B_inv:
    print(row)

print("\nResult of A ÷ B (A * B^-1):")
for row in result:
    print(row)
    

print("\nChoose operation:")
print("1. Addition (A + B)")
print("2. Subtraction (A - B)")
print("3. Multiplication (A * B)")
print("4. Division (A * B^-1)")

choice = int(input("Enter choice(1-4): "))

if choice == 1:
    result = add_matrix(A, B)
elif choice == 2:
    result = sub_matrix(A, B)
elif choice == 3:
    result = multi_matrix(A, B)
elif choice == 4:
    B_inv = inverse_matrix(B)
    result = multiply_matrix(A, B_inv)
else:
    print("Invalid choice")
    result = None

if result:
    print("\nResult:")
    for row in result:
        print(row)