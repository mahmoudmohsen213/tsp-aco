import sys, csv, math

# convert a dataset file from euclidean distance format to graph format
inputFileName = sys.argv[1]
outputFileName = sys.argv[2]

with open(inputFileName) as inputFile:
  csvFile = csv.reader(inputFile, delimiter=',')
  nodesData = []
  for csvRow in csvFile:
    row = []
    for entry in csvRow:
      row.append(float(entry))
    nodesData.append(row)
inputFile.close()

nodes = len(nodesData)

outputFile = open(outputFileName, 'w')
outputFile.write(str(nodes) + ' ' + str(int((nodes * (nodes - 1)) / 2)) + '\n')

for i in range(nodes):
  for j in range(i + 1, nodes):
    p1 = (nodesData[i][0], nodesData[i][1])
    p2 = (nodesData[j][0], nodesData[j][1])
    d = math.sqrt(sum([(a - b)** 2 for a, b in zip(p1, p2)]))
    outputFile.write(str(i) + ' ' + str(j) + ' ' + str(d) + '\n')

outputFile.close()
