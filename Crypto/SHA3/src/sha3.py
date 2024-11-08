import numpy as np

# Round constants for the iota function
round_constants = [
    0x0000000000000001, 0x0000000000008082, 0x800000000000808A,
    0x8000000080008000, 0x000000000000808B, 0x0000000080000001,
    0x8000000080008081, 0x8000000000008009, 0x000000000000008A,
    0x0000000000000088, 0x0000000080008009, 0x000000008000000A,
    0x000000008000808B, 0x800000000000008B, 0x8000000000008089,
    0x8000000000008003, 0x8000000000008002, 0x8000000000000080,
    0x000000000000800A, 0x800000008000000A, 0x8000000080008081,
    0x8000000000008080, 0x0000000080000001, 0x8000000080008008
]

def convert_array_to_3D(S):
    # Initialize an empty array and convert 1D to 3D
    A = np.zeros((5, 5, 64), dtype=int)
    for i in range(5):
        for j in range(5):
            for k in range(64):
                A[i][j][k] = S[64 * (5 * j + i) + k]
    return A

def convert_array_to_1D(A):
    # Initialize a 1600-bit 1D array
    S = np.zeros(1600, dtype=int)
    for i in range(5):
        for j in range(5):
            for k in range(64):
                S[64 * (5 * j + i) + k] = A[i][j][k]
    return S

def theta(A):
    A_prime = np.zeros((5, 5, 64), dtype=int)
    # Calculate the parity array for the columns
    C = np.zeros((5, 64), dtype=int)
    for i in range(5):
        for k in range(64):
            C[i][k] = A[i][0][k] ^ A[i][1][k] ^ A[i][2][k] ^ A[i][3][k] ^ A[i][4][k]
    # Apply the theta transformation
    for i in range(5):
        for j in range(5):
            for k in range(64):
                D_i_k = C[(i-1) % 5][k] ^ np.roll(C[(i+1) % 5], 1)[k]
                A_prime[i][j][k] = A[i][j][k] ^ D_i_k
    return A_prime

def rho(A):
    # Rotation offsets for each position (i, j)
    rotation_offsets = [
        [0,  36, 3,  41, 18],
        [1,  44, 10, 45, 2],
        [62, 6,  43, 15, 61],
        [28, 55, 25, 21, 56],
        [27, 20, 39, 8,  14]
    ]
    A_prime = np.zeros((5, 5, 64), dtype=int)
    for i in range(5):
        for j in range(5):
            rotation = rotation_offsets[i][j]
            A_prime[i][j] = np.roll(A[i][j], -rotation)
    return A_prime

def pi(A):
    A_prime = np.zeros((5, 5, 64), dtype=int)
    for i in range(5):
        for j in range(5):
            new_i = j
            new_j = (2 * i + 3 * j) % 5
            A_prime[new_i][new_j] = A[i][j]
    return A_prime

def chi(A):
    A_prime = np.zeros((5, 5, 64), dtype=int)
    for j in range(5):
        for i in range(5):
            for k in range(64):
                A_prime[i][j][k] = A[i][j][k] ^ ((~A[(i + 1) % 5][j][k]) & A[(i + 2) % 5][j][k])
    return A_prime

def iota(A, round_index):
    for k in range(64):
        A[0][0][k] ^= (round_constants[round_index] >> k) & 1
    return A

def sha3(S):
    A = convert_array_to_3D(S)
    for round_index in range(24):
        A = theta(A)
        A = rho(A)
        A = pi(A)
        A = chi(A)
        A = iota(A, round_index)
    S_prime = convert_array_to_1D(A)
    return S_prime

def main():
    np.set_printoptions(threshold=np.inf)
    random_ass_array = np.random.randint(0, 2, 1600, dtype=int)
    print("\nOriginal 1D array:")
    print(random_ass_array)

    print("\n****************************************************************************\n")

    result = sha3(random_ass_array)
    print("SHA3 transformed 1D array:")
    print(result)

if __name__ == "__main__":
    main()
