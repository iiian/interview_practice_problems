def count_unique_paths_in_grid(grid) -> int:
    if grid[0][0] == 1: return 0
    grid[0][0] = 1
    for x in range(1, len(grid[0])):
        if grid[0][x] == 0:
            grid[0][x] = grid[0][x-1]
        else:
            grid[0][x] = 0
    for y in range(1, len(grid)):
        if grid[y][0] == 0:
            grid[y][0] = grid[y-1][0]
    for y in range(1, len(grid)):
        for x in range(1, len(grid[0])):
            if grid[y][x] == 1:
                grid[y][x] = 0
            else:
                grid[y][x] = grid[y-1][x] + grid[y][x-1]
    return grid[y][x]

if __name__ == '__main__':
    grid =  [
        [0,1],
        [0,1],
        [0,1],
        [0,0],
    ]
    assert count_unique_paths_in_grid(grid) == 1, f'was count_unique_paths_in_grid (1) {count_unique_paths_in_grid(grid)}'
    grid =  [
        [0,1],
        [0,1],
        [0,0],
        [0,0],
    ]
    assert count_unique_paths_in_grid(grid) == 2
    grid = [
        [0,1,0,0],
        [0,1,0,0],
        [0,0,0,1],
        [0,0,1,0],
    ]
    assert count_unique_paths_in_grid(grid) == 0
    grid = [
        [0,1,0,0],
        [0,1,0,0],
        [0,0,0,1],
        [0,0,0,0],
    ]
    actual = count_unique_paths_in_grid(grid)
    assert actual == 4, f'was {actual}'