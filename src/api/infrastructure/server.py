from typing import Dict
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

def response (res_object: Dict):
    r = res_object.copy()
    def apply_response (res: Dict) -> Dict:
        r.update(res)
        return r
    
    return apply_response

@app.post('/solver')
async def solver(file: UploadFile = File(), parameters: str = Form()):
    params = json.loads(parameters)
    resolution_algorithm = params['algorithm']

    (nodes, edges) = await parseMaze(file.file)
    node_start = params['start']
    node_end = params['end']

    res = response({
        'nodes': nodes,
        'edges': edges,
    })

    if resolution_algorithm == 'bfs':
        from algorithms.anchura import Graph as BFSGraph
        g = BFSGraph()
        for node in nodes:
            g.add_node(node)
        for (e1, e2) in edges:
            g.add_edge(e1, e2)

        return res(g.BFS(node_start, node_end))

    if resolution_algorithm == 'dfs':
        from algorithms.profundidad import Graph as DFSGraph
        g = DFSGraph()
        for node in nodes:
            g.add_node(node)
        for (e1, e2) in edges:
            g.add_edge(e1, e2)

        return res(g.DFS(node_start, node_end))
        
    if resolution_algorithm == 'depth_iterative':
        from algorithms.anchura import Graph as BFSGraph
        g = BFSGraph()
        for node in nodes:
            g.add_node(node)
        for (e1, e2) in edges:
            g.add_edge(e1, e2)

        return res(g.BFS(node_start, node_end))
        
    if resolution_algorithm == 'uniform_cost':
        from algorithms.costo_uniforme import Graph as UCSGraph
        g = UCSGraph()
        for node in nodes:
            g.add_node(node)
        for (e1, e2) in edges:
            g.add_edge(e1, e2)

        return res(g.UCS(node_start, node_end))

    if resolution_algorithm == 'greedy':
        from algorithms.greedy import Graph as GreedyGraph
        g = GreedyGraph()
        for node in nodes:
            g.add_node(node)
        for (e1, e2) in edges:
            g.add_edge(e1, e2)

        return res(g.greedy(node_start, node_end))
        
    elif resolution_algorithm == 'astar':
        from algorithms.a_star import Graph as AStarGraph

        g = AStarGraph()
        for node in nodes:
            g.add_node(node)
        for (e1, e2) in edges:
            g.add_edge(e1, e2)

        return res(g.astar(node_start, node_end))
    
    return { "hello": "world" }