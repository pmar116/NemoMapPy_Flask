from app.Graph import Graph
import sys
class GraphProcessor:
    """
        A Class to read a graph from a file.
        File should be formatted:
            'first#ofEdge1 second#ofEdge1
            first#ofEdge2 second#ofEdge2 . . .'

        Methods
        -------
        loadGraph
            reads edges from a text file and stores the values in a 2D list
        """
    def __init__(self):
        pass
    def loadGraph(self, grapharray):
        """
        loadGraph: reads edges from a text file and stores the values in a 2D list
        :param fileName:string The name f the file containing the graph edges
        :return: Graph - A graph containing the edges from the file
        """
        edgeList = []
        for line in grapharray:
            #print(line, file=sys.stderr)
            if "#" not in line:     #catch comments
                pair = [int(i) for i in line.split()]   #read in as integers
                if pair[0] != pair[1]:
                    edgeList.append(pair)

        newGraph = Graph(edgeList)
        return newGraph