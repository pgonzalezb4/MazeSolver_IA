from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware

import json

from domain.maze import parseMaze
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['POST'],
    allow_headers=['Content-Type'],
)

@app.post('/solver')
async def solver(file: UploadFile = File(), parameters: str = Form()):
    params = json.loads(parameters)
    
    resolution_algorithm = params['algorithm']

    (nodes, edges) = await parseMaze(file.file)
    node_start = params['start']
    node_end = params['end']

    if resolution_algorithm == 'bfs':
        # TODO: Load and resolve by BFS
        pass
    if resolution_algorithm == 'dfs':
        # TODO: Load and resolve by DFS
        pass
    if resolution_algorithm == 'depth_iterative':
        # TODO: Load and resolve by Depth Iterative
        pass
    if resolution_algorithm == 'uniform_cost':
        # TODO: Load and resolve by Uniform Cost
        pass
    if resolution_algorithm == 'greedy':
        # TODO: Load and resolve by Greedy
        pass
    elif resolution_algorithm == 'astar':
        # TODO: Load and resolve by AStar
        pass
    
    return { "hello": "world" }