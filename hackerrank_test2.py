def minCost(rows, cols, initR, initC, finalR, finalC, costRows, costCols):
    # Write your code here
    count = 0
    if finalR > initR:
        row_list = list(range(initR, finalR))
    else:
        row_list = list(range(finalR, initR-1, -1))
    if finalC > initC:
        col_list = list(range(initR, finalR+1))
    else:
        col_list = list(range(finalR,initR-1,-1))
    print(row_list)
    print(col_list)
    for r in row_list:
        print(r)
        count += costRows[r]
    for c in col_list:
        print(c)
        count += costCols[c]
    return count

rows = 3
cols = 3
initR = 0
initC = 0
finalR = 1
finalC = 2
costRows = [2,5]
costCols = [6,1]
print(minCost(rows, cols, initR, initC, finalR, finalC, costRows, costCols))