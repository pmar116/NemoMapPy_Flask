import time
from app.GraphProcessor import GraphProcessor
from app.Utility import Utility
from flask import jsonify
import sys

def nmp(inputg, queryg):
    myGP = GraphProcessor()
    inputGraph = myGP.loadGraph(inputg)
    queryGraph = myGP.loadGraph(queryg)
    myUtility = Utility()

    h = queryGraph.getNodesSortedByDegree(0)
    h1 = h[-1]

    timeStart = time.time()
    totalMappings = myUtility.algorithm2_modified(queryGraph, inputGraph, h1)
    timeEnd = time.time()

    data=[]
    data.append({"mappings":totalMappings})
    data.append({"runtime":(timeEnd-timeStart)})
    return data