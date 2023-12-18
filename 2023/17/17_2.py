from heapq import heappush, heappop

def parse_input(filename):
    with open(filename, 'r') as f:
        return [[int(x) for x in line.rstrip('\n')] for line in f.readlines()]

def add(lines, queue, heat_loss: int, row: int, col: int, row_diff: int, col_diff: int, steps: int = 1):
    new_row = row + row_diff
    new_col = col + col_diff
    if not (0 <= new_row < len(lines) and 0 <= new_col < len(lines[new_row])):
        return
    heappush(
        queue,
        (
            heat_loss + lines[new_row][new_col],
            new_row,
            new_col,
            row_diff,
            col_diff,
            steps,
        ),
    )

def search(lines):
    visited = set()
    priority_queue = [(0, 0, 0, 0, 0, 0)]
    while priority_queue:
        heat_loss, row, col, row_diff, col_diff, steps = heappop(priority_queue)
        if steps >= 4 and row == len(lines) - 1 and col == len(lines[0]) - 1:
            return heat_loss
        if (row, col, row_diff, col_diff, steps) in visited:
            continue
        visited.add((row, col, row_diff, col_diff, steps))
        if steps < 10 and (row_diff, col_diff) != (0, 0):
            add(lines, priority_queue, heat_loss, row, col, row_diff, col_diff, steps + 1)
        if steps >= 4 or (row_diff, col_diff) == (0, 0):
            for r, c in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if (r, c) != (row_diff, col_diff) and (r, c) != (-row_diff, -col_diff):
                    add(lines, priority_queue, heat_loss, row, col, r, c)

def get_answer(filename='input.txt'):
    lines = parse_input('2023/17/'+filename)
    answer = search(lines)
    return answer

answer = get_answer()#'test_input.txt')
print(answer)