from largest_rectangle_in_histogram import largest_rectangle_in_histogram

def max_rectangle_bin_matrix(matrix):
    cursor = [0 for _ in matrix[0]]
    max_area = 0
    for r in range(len(matrix)):
        next_row = matrix[r]
        for c in range(len(cursor)):
            cursor[c] = 0 if next_row[c] == 0 else cursor[c] + next_row[c]
        max_area = max(
            largest_rectangle_in_histogram(cursor),
            max_area
        )

    return max_area

if __name__ == "__main__":
    from testing import test_case
    test_case(
        '(1) it should return the max area of the largest rectangle made of all 1s in a binary matrix',
        max_rectangle_bin_matrix(
            [
                [0,0,1,1,1,0],
                [0,0,1,1,1,0],
                [0,1,1,1,1,0],
                [1,1,1,1,1,1],
                [0,0,1,0,1,0],
            ]
        ),
        12
    )

    test_case(
        '(2) it should return the max area of the largest rectangle made of all 1s in a binary matrix',
        max_rectangle_bin_matrix(
            [
                [0,0,1,1,1,0],
                [0,0,1,1,1,0],
                [0,1,1,1,1,0],
            ]
        ),
        9
    )

    test_case(
        '(3) it should return the max area of the largest rectangle made of all 1s in a binary matrix',
        max_rectangle_bin_matrix(
            [
                [0,0,1,1,],
                [0,0,1,1,],
                [0,1,1,1,],
            ]
        ),
        6
    )