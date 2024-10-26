board = [
    ["@", "X", "@"],
    ["@", "@", "@"],
    ["X", "@", "X"]
]

# def printBoard(board): # old
#     print("-" * 19)
#     for row in range(len(board[0])):
#         for col in range(len(board)):
#             print("| ", board[row][col], end="  ")
#         print("|")
#         print("-" * 19)
        
def printBoard(board):
    print("-" * 19)
    for row in board:
        for space in row:
            print("| ", space, end="  ")
        print("|", getRowDef(row))
        print("-" * 19)
    getColDefs(board)

def getRowDef(row):
    # print(row)
    rowDef = []
    spaceCount = 0
    for space in row:
        # print(space)
        if (space == 'X'):
            if (spaceCount != 0):
                rowDef.append(spaceCount)
                spaceCount = 0
        else:
            spaceCount += 1
        # print("spaceCount =", spaceCount)
        # print("---")
    if (spaceCount != 0):
        rowDef.append(spaceCount)
        spaceCount = 0
    # print("rowDef =", rowDef)
    # print()
    # break
    return rowDef

def getColDefs(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(row, col)

printBoard(board)

# getRowDef(board)