def rot_mat(mat):
    if not len(mat):
        return

    tp = 0
    btm = len(mat)-1

    left = 0
    right = len(mat[0])-1

    while left < right and tp < btm:
        prev = mat[tp+1][left]
        for i in range(left, right+1):
            curr = mat[tp][i]
            mat[tp][i] = prev
            prev = curr

        tp += 1
        for i in range(tp, btm+1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr

        right -= 1
        for i in range(right, left-1, -1):
            curr = mat[btm][i]
            mat[btm][i] = prev
            prev = curr

        btm -= 1
        for i in range(btm, tp-1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr

        left += 1

    return mat


def print_mat(mat):
    for row in mat:
        print(row)

if __name__ == '__main__':
    matrix =[
            [1,  2,  3,  4 ],
            [5,  6,  7,  8 ],
            [9,  10, 11, 12 ],
            [13, 14, 15, 16 ]
        ]
    #mat2 =[
    #    [1,2,3,4,5],
    #    [6,7,8,9],8,
    #    [10,11,23,9,0],
    #    [54,87,90,12,98],
    #    [34,56,78,12,67]
    #]
    matrix = rot_mat(matrix)
    print_mat(matrix)
