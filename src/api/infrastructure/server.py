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
        from algorithms.costo_uniforme import Graph as UCSGraph
        g = UCSGraph()
        for node in nodes:
            g.add_node(node)
        for (e1, e2) in edges:
            g.add_edge(e1, e2)

        return g.UCS(node_start, node_end)

    if resolution_algorithm == 'greedy':
        from algorithms.greedy import Graph as GreedyGraph
        g = GreedyGraph()
        for node in nodes:
            g.add_node(node)
        for (e1, e2) in edges:
            g.add_edge(e1, e2)

        return g.greedy(node_start, node_end)
        
    elif resolution_algorithm == 'astar':
        from algorithms.a_star import Graph as AStarGraph

        g = AStarGraph()
        for node in nodes:
            g.add_node(node)
        for (e1, e2) in edges:
            g.add_edge(e1, e2)

        return g.astar(node_start, node_end)
    
    return { "hello": "world" }