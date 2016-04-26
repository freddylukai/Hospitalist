from Graph import Graph
from opNode import opNode
from graphGen import genGraph
from cpl import calcCPLs, schedule, getCPL

def opSeq(recipeNode):
    graph = genGraph(recipeNode)
    topOrder =(calcCPLs(graph, recipeNode))
    sortedCPLs = list(sorted(topOrder, key=getCPL, reverse=True))
    optimalOrder = schedule(sortedCPLs, recipeNode)

    for s in optimalOrder:
        print("node: " + str(s.idx) + "cpl: " + str(s.cpl))

if __name__ == "__main__":

 ## Test 1

 children1 = set()
 children2 = set()
 children3 = set()
 children4 = set()
 children5 = set()
 children6 = set()
 children7 = set()
 children8 = set()
 children9 = set()
 children10 = set()
 children11 = set()
 children12 = set()
 children13 = set()
 children14 = set()


 rootNode1 = opNode(14, children14, 0) 
 onode_13 = opNode(13, children13, 15) 
 onode_12 = opNode(12, children12, 10) 
 onode_11 = opNode(11, children11, 5)  
 onode_10 = opNode(10, children10, 2400)  
 onode_9 = opNode(9, children9, 3600)  
 onode_8 = opNode(8, children8, 30)  
 onode_7 = opNode(7, children7, 20) 
 onode_6 = opNode(6, children6, 20)  
 onode_5 = opNode(5, children5, 10)  
 onode_4 = opNode(4, children4, 60)  
 onode_3 = opNode(3, children3, 20)  
 onode_2 = opNode(2, children2, 20)  
 onode_1 = opNode(1, children1, 600)  

 rootNode1.add_child(onode_13)
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


 ## ------------------------------------------------------------------------

 ## Test 2
 children1 = set()
 children2 = set()
 children3 = set()
 children4 = set()
 children5 = set()
 children6 = set()
 children7 = set()

 rootNode2 = opNode(7, children7, 0) 
 onode_6 = opNode(6, children6, 180)  
 onode_5 = opNode(5, children5, 120)  
 onode_4 = opNode(4, children4, 60)  
 onode_3 = opNode(3, children3, 60)  
 onode_2 = opNode(2, children2, 600)  
 onode_1 = opNode(1, children1, 20)  

 rootNode2.add_child(onode_6)
 onode_6.add_child(onode_5)
 onode_6.add_child(onode_2)
 onode_5.add_child(onode_3)
 onode_5.add_child(onode_4)
 onode_2.add_child(onode_1)

 ## ------------------------------------------------------------------------

 ##Test3
 children1 = set() 
 children2 = set()
 children3 = set()
 children4 = set()
 children5 = set()
 children6 = set()
 children7 = set()
 children8 = set()
 children9 = set()

 rootNode3 = opNode(9, children9, 0)
 onode_8 = opNode(8, children8, 1800) 
 onode_7 = opNode(7, children7, 600)  
 onode_6 = opNode(6, children6, 20)  
 onode_5 = opNode(5, children5, 600) 
 onode_4 = opNode(4, children4, 60)  
 onode_3 = opNode(3, children3, 20)  
 onode_2 = opNode(2, children2, 20)  
 onode_1 = opNode(1, children1, 20)  

 rootNode3.add_child(onode_8)
 onode_8.add_child(onode_6)
 onode_8.add_child(onode_5)
 onode_7.add_child(onode_4)
 onode_6.add_child(onode_1)
 onode_6.add_child(onode_7)
 onode_5.add_child(onode_3)
 onode_4.add_child(onode_2)

 ## ------------------------------------------------------------------------

 ##Test 4
 children1 = set() 
 children2 = set() 
 children3 = set() 
 children4 = set() 
 children5 = set() 
 children6 = set() 
 children7 = set() 
 children8 = set() 
 children9 = set() 
 children10 = set() 
 children11 = set() 
 children12 = set() 
 children13 = set() 

 rootNode4 = opNode(13, children13, 0) 
 onode_12 = opNode(12, children12, 1200) 
 onode_11 = opNode(11, children11, 60)  
 onode_10 = opNode(10, children10, 2400)  
 onode_9 = opNode(9, children9, 60) 
 onode_8 = opNode(8, children8, 3000)  
 onode_7 = opNode(7, children7, 30) 
 onode_6 = opNode(6, children6, 600) 
 onode_5 = opNode(5, children5, 10)  
 onode_4 = opNode(4, children4, 300)  
 onode_3 = opNode(3, children3, 20)  
 onode_2 = opNode(2, children2, 20)  
 onode_1 = opNode(1, children1, 30)  

 rootNode4.add_child(onode_12)
 onode_12.add_child(onode_11)
 onode_11.add_child(onode_10)
 onode_11.add_child(onode_7)
 onode_10.add_child(onode_9)
 onode_9.add_child(onode_8)
 onode_8.add_child(onode_5)
 onode_7.add_child(onode_4)
 onode_6.add_child(onode_3)
 onode_5.add_child(onode_2)
 onode_5.add_child(onode_6)
 onode_4.add_child(onode_1)

 opSeq(rootNode1)
 print(" ")
 opSeq(rootNode2)
 print(" ")
 opSeq(rootNode3)
 print(" ")
 opSeq(rootNode4)
 print(" ")