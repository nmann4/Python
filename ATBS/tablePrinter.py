#! python3
# tablePrinter.py - prints lists in a well-organized table

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


colWidth = [0] * len(tableData)

for i in xrange(len(tableData)):
    for k in xrange(len(tableData[i])):
            if colWidth[i] < len(tableData[i][k]):
                colWidth[i] = len(tableData[i][k])


for i in xrange(len(tableData[0])):
    print(tableData[0][i].rjust(colWidth[0]) + ' ' + 
          tableData[1][i].rjust(colWidth[1]) + ' ' + 
          tableData[2][i].rjust(colWidth[2]))
