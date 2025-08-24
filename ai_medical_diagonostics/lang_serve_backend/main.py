from fastapi import FastAPI
from langserve import add_routes
from diagnostics_graph import build_graph

graph=build_graph()
api=FastAPI()
add_routes(api, graph, path="/diagnostics")



 
