from typing import BinaryIO

async def parseMaze (file: BinaryIO):
    matrix = []
    
    for line in file.readlines():
        line = line.replace(b'\r\n', b'')
        line = line.replace(b'\r', b'')

        row = []
        for cell in line.split(b','):
            row.append(cell == b'c')

        matrix.append(row)

    nodes = []
    edges = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]:
                nodes.append((i, j))
                
                if i + 1 < len(matrix) and matrix[i + 1][j]:
                    edges.append(((i, j), (i + 1, j)))
                
                if j + 1 < len(matrix[i]) and matrix[i][j + 1]:
                    edges.append(((i, j), (i, j + 1)))
    
    return (nodes, edges)
