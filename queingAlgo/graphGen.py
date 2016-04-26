from opNode import opNode
from Graph import Graph
import queue
##import Queue



def genGraph(recipeNode):
    g = {recipeNode: set(recipeNode.children)}
    nodeQueue = queue.Queue()
    curNode = recipeNode
    graph = Graph(g)

    for n in recipeNode.children:
        nodeQueue.put(n)
        graph.add_vertex(n);
        #print( str(n.idx)  + "is a child of " + str(recipeNode.idx))


    while (not nodeQueue.empty()):
        curNode = nodeQueue.get()
        for d in curNode.children:
            nodeQueue.put(d); 
            graph.add_vertex(d);
            graph.add_edge({curNode, d})
            #print( str(d.idx)  + "is a child of " + str(curNode.idx))
            
    return graph

if __name__ == "__main__":

     children1 = Set([]) 
     children2 = Set([])
     children3 = Set([])
     children4 = Set([])
     children5 = Set([])
     children6 = Set([])
     children7 = Set([])
     children8 = Set([])
     children9 = Set([])
     children10 = Set([])
     children11 = Set([])
     children12 = Set([])
     children13 = Set([])
     children14 = Set([])


     recipeNode = opNode(14, children14, 0, False) 
     onode_13 = opNode(13, children13, 15, False) ##oranges
     onode_12 = opNode(12, children12, 10, False) ##garnish
     onode_11 = opNode(11, children11, 5, False)  ##pile
     onode_10 = opNode(10, children10, 2400, True)  ##bake
     onode_9 = opNode(9, children9, 3600, True)  ##marinate
     onode_8 = opNode(8, children8, 30, False)  ##massage
     onode_7 = opNode(7, children7, 20, False)  ##arrange on sheet
     onode_6 = opNode(6, children6, 20, False)  ##pour sauce on wings
     onode_5 = opNode(5, children5, 10, False)  ##season wings
     onode_4 = opNode(4, children4, 60, False)  ##dry wings
     onode_3 = opNode(3, children3, 20, False)  ##rinse wings
     onode_2 = opNode(2, children2, 20, False)  ##mix sauce
     onode_1 = opNode(1, children1, 600, True)  ##preheat oven
        

     recipeNode.add_child(onode_13)
     onode_13.add_child(onode_12)
     onode_12.add_child(onode_11)
     onode_11.add_child(onode_10)
     onode_10.add_child(onode_7)
     onode_10.add_child(onode_9)
     onode_9.add_child(onode_8)
     onode_9.add_child(onode_7)
     onode_8.add_child(onode_6)
     onode_7.add_child(onode_1)
     onode_6.add_child(onode_2)
     onode_6.add_child(onode_5)
     onode_5.add_child(onode_4)
     onode_4.add_child(onode_3)

     graph = genGraph(recipeNode)

     print("Vertices of graph:")
     dependencies = graph.vertices()
     for d in dependencies:
        print(d.idx)

     print("edges of graph:")
     edges = graph.edges()
     for i in edges:
        for node in i:
            print(node.idx),
        print (" ")