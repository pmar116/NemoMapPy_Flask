import time
from app.GraphProcessor import GraphProcessor
from app.Utility import Utility
from flask import jsonify
import sys

def nmp(inputg, queryg):
    #print("\nrunning nemomappy...")

    myGP = GraphProcessor()
    inputGraph = myGP.loadGraph(inputg)
    queryGraph = myGP.loadGraph(queryg)
    myUtility = Utility()

    #print("Input Graph: Nodes - %d; Edges - %d" % (inputGraph.getNumberofVertices(), inputGraph.getNumberofEdges()))
    #print("Query Graph: Nodes - %d; Edges - %d" % (queryGraph.getNumberofVertices(), queryGraph.getNumberofEdges()))

    h = queryGraph.getNodesSortedByDegree(0)
    h1 = h[-1]
    #print("\nH node = [ %d ]" % h1)

    timeStart = time.time()
    totalMappings = myUtility.algorithm2_modified(queryGraph, inputGraph, h1)
    timeEnd = time.time()
    #print("\nMapping: %d" % totalMappings)
    #print("Time taken: %s seconds\n" % (timeEnd-timeStart))

    #data={"mappings":totalMappings, "runtime":(timeEnd-timeStart)}
    data=[]
    data.append({"mappings":totalMappings})
    data.append({"runtime":(timeEnd-timeStart)})
    return data