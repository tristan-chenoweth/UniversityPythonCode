def is_complete(grid):
    good_set = set([1,2,3,4,5,6,7,8,9])

    for row in grid:
        #print(row)
        if set(row)!= good_set:
            return False

    print('')

    for c in range(9):
        #print([row[c] for row in grid])
        if set([row[c] for row in grid]) != good_set:
            return False


    print('')

    for r in [0 , 3 , 6]:
        for c in [0 , 3 , 6]:
            #print(grid[r][c:c+3] + grid[r+1][c:c+3] + grid[r+2][c:c+3])
            if set(grid[r][c:c+3] + grid[r+1][c:c+3] + grid[r+2][c:c+3]) != good_set:
                return False

    return True



def get_row(grid , r):
    return grid[r]

def get_column(grid , c):
    return [row[c] for row in grid]

def get_box(grid , r , c):
    r = r - (r % 3)
    c = c - (c % 3)    
    return grid[r][c:c+3] + grid[r+1][c:c+3] + grid[r+2][c:c+3]

def get_ava_numbers(grid , r , c):
    all_numbers = set([1,2,3,4,5,6,7,8,9])
    row_numbers = set(get_row(grid, r))
    column_numbers = set(get_column(grid, c))
    box_numbers = set(get_box(grid, r , c))

    return all_numbers - row_numbers - column_numbers - box_numbers

def get_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i,j)

    return (-1,-1)



def show(grid):
    for r in grid:
        print(r)



def solve(grid):
    if is_complete(grid):
        return True
    
    
    r , c = get_empty_cell(grid)
    
    ava_numbers = get_ava_numbers(grid , r , c)


    for n in ava_numbers:
        grid[r][c] = n
        if solve(grid):
            #show(grid)
            return True
    grid[r][c] = 0
    return False

    


fin = open('sudoku_problem_5.txt') #change to problem to check for available numbers and solution to check solution
grid = []

for line in fin:
    #print(line , end='')
    row = [eval(n) for n in line.split()]
    #print(row)
    grid.append(row)


solve(grid)
show(grid)

# print(is_complete(grid))


# print(get_ava_numbers(grid , 0 , 1))

# print(get_empty_cell(grid))
