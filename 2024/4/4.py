def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]

def p1(filename):
    rows = read_lines(filename)
    cols = [''.join([row[i] for row in rows]) for i in range(len(rows[0]))]
    count = sum(line.count('XMAS') + line.count('SAMX') for line in rows + cols)

    for i in range(len(rows)):
        for j in range(len(rows[0])):
            diag1 = ''.join(rows[i + k][j + k] for k in range(4)) if j + 3 < len(rows[0]) and i + 3 < len(rows) else ''
            diag2 = ''.join(rows[i + k][j - k] for k in range(4) if j - k >= 0) if j - 3 >= 0 and i + 3 < len(rows) else ''
            count += (diag1 in {'XMAS', 'SAMX'}) + (diag2 in {'XMAS', 'SAMX'})
    return count


    # rows = read_lines(filename)
    # cols = [''.join([row[i] for row in rows]) for i in range(len(rows[0]))]
    # # diagonals = [''.join([row[i] for i, row in enumerate(rows)]), ''.join([row[-i-1] for i, row in enumerate(rows)])]
    # count = 0
    # for l in rows + cols:
    #     count += l.count('XMAS')
    #     count += l.count('SAMX')
    
    # for i in range(len(rows)):
    #     for j in range(len(rows[0])):
    #         if i + 3 < len(rows) and j + 3 < len(rows[0]):
    #             count += rows[i][j] + rows[i+1][j+1] + rows[i+2][j+2] + rows[i+3][j+3] == 'XMAS'
    #             count += rows[i][j] + rows[i+1][j+1] + rows[i+2][j+2] + rows[i+3][j+3] == 'SAMX'
    #         if i + 3 < len(rows) and j - 3 >= 0:
    #             count += rows[i][j] + rows[i+1][j-1] + rows[i+2][j-2] + rows[i+3][j-3] == 'XMAS'
    #             count += rows[i][j] + rows[i+1][j-1] + rows[i+2][j-2] + rows[i+3][j-3] == 'SAMX'
    # return count
    
        

def p2(filename):
    rows = read_lines(filename)
    count = 0
    for i in range(1, len(rows) - 1):
        for j in range(1, len(rows[0]) - 1):
            if rows[i][j] == 'A':
                count += rows[i - 1][j - 1] + rows[i][j] + rows[i + 1][j + 1] in {'MAS', 'SAM'} and rows[i - 1][j + 1] + rows[i][j] + rows[i + 1][j - 1] in {'MAS', 'SAM'}
    # for i in range(len(rows)):
    #     for j in range(len(rows[0])):
    #         if rows[i][j] == 'A' and i + 1 < len(rows) and j + 1 < len(rows[0]) and i > 0 and j > 0:
    #             count += rows[i+1][j+1] + rows[i][j] + rows[i-1][j-1] == 'MAS' and (rows[i+1][j-1] + rows[i][j] + rows[i-1][j+1] == 'MAS' or rows[i-1][j+1] + rows[i][j] + rows[i+1][j-1] == 'MAS')
    #             count += rows[i+1][j+1] + rows[i][j] + rows[i-1][j-1] == 'SAM' and (rows[i+1][j-1] + rows[i][j] + rows[i-1][j+1] == 'SAM' or rows[i-1][j+1] + rows[i][j] + rows[i+1][j-1] == 'SAM')
    return count


print(p1('2024/4/input.txt'))
print(p2('2024/4/input.txt'))