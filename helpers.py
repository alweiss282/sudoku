from random import randint

def generate_grid(arr, BOX_SIZE):
    """
    Generates valid and solvable sudoku grid. Uses randomization to "solve" the
    sudoku, and backtracking to efficiently check possibilities.
    """
    l = [0, 0]

    if not find_empty_location(arr, l, BOX_SIZE):
        return True

    row = l[0]
    col = l[1]

    used = set()
    while len(used) != BOX_SIZE**2:
        num = randint(1, BOX_SIZE**2)
        if check_location_is_safe(arr, row, col, num, BOX_SIZE):
            arr[row][col] = num

            if generate_grid(arr, BOX_SIZE):
                return True
            # This assignment failed – undo it and retry
            arr[row][col] = 0
        used.add(num)

    return False


def find_empty_location(arr, l, BOX_SIZE):
    for row in range(BOX_SIZE**2):
        for col in range(BOX_SIZE**2):
            if(arr[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False


def check_location_is_safe(arr, row, col, num, BOX_SIZE):
    return (not used_in_row(arr, row, num, BOX_SIZE) and
            not used_in_col(arr, col, num, BOX_SIZE) and
            not used_in_box(arr, row - row % BOX_SIZE, col - col % BOX_SIZE, num, BOX_SIZE))


def used_in_row(arr, row, num, BOX_SIZE):
    for i in range(BOX_SIZE**2):
        if arr[row][i] == num:
            return True
    return False


def used_in_col(arr, col, num, BOX_SIZE):
    for i in range(BOX_SIZE**2):
        if arr[i][col] == num:
            return True
    return False


def used_in_box(arr, row, col, num, BOX_SIZE):
    for i in range(BOX_SIZE):
        for j in range(BOX_SIZE):
            if arr[i+row][j+col] == num:
                return True
    return False


def remove_k_digits(arr, k, BOX_SIZE):
    count = k
    while count != 0:
        i = randint(0, BOX_SIZE**2-1)
        j = randint(0, BOX_SIZE**2-1)
        if arr[i][j] != 0:
            count -= 1
            arr[i][j] = 0
