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

 ## CHICKEN WINGS

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


 recipeNode1 = opNode(14, children14, 0, False) 
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
    

 recipeNode1.add_child(onode_13)
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

 ## DEVILS ON HORSEBACK
 children1 = set()
 children2 = set()
 children3 = set()
 children4 = set()
 children5 = set()
 children6 = set()
 children7 = set()

 recipeNode2 = opNode(7, children7, 0, False) ##devils on horseback
 onode_6 = opNode(6, children6, 180, True)  ##bake bacon
 onode_5 = opNode(5, children5, 120, False)  ##wrap bacon
 onode_4 = opNode(4, children4, 60, False)  ##pit prunes
 onode_3 = opNode(3, children3, 60, False)  ##slice bacon
 onode_2 = opNode(2, children2, 600, True)  ##preheat oven
 onode_1 = opNode(1, children1, 20, False)  ##Turn on oven

 recipeNode2.add_child(onode_6)
 onode_6.add_child(onode_5)
 onode_6.add_child(onode_2)
 onode_5.add_child(onode_3)
 onode_5.add_child(onode_4)
 onode_2.add_child(onode_1)

 ## ------------------------------------------------------------------------

 ##CARAMALIZED ONION AND KIELBASA TARTS
 children1 = set() 
 children2 = set()
 children3 = set()
 children4 = set()
 children5 = set()
 children6 = set()
 children7 = set()
 children8 = set()
 children9 = set()

 recipeNode3 = opNode(9, children9, 0, False) ##tarts
 onode_8 = opNode(8, children8, 1800, True) ##bake tarts
 onode_7 = opNode(7, children7, 600, True)  ##cook onions
 onode_6 = opNode(6, children6, 20, False)  ##unroll puffs
 onode_5 = opNode(5, children5, 600, True)  ##preheat oven
 onode_4 = opNode(4, children4, 60, False)  ##onions on stove
 onode_3 = opNode(3, children3, 20, False)  ##turn on stove
 onode_2 = opNode(2, children2, 20, False)  ##dice onions
 onode_1 = opNode(1, children1, 20, True)  ##grate cheese

 recipeNode3.add_child(onode_8)
 onode_8.add_child(onode_6)
 onode_8.add_child(onode_5)
 onode_7.add_child(onode_4)
 onode_6.add_child(onode_1)
 onode_6.add_child(onode_7)
 onode_5.add_child(onode_3)
 onode_4.add_child(onode_2)

 ## ------------------------------------------------------------------------

 ##STRAWBERRY PRETZEL SALAD
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

 recipeNode4 = opNode(13, children13, 0, False) ##SALAD
 onode_12 = opNode(12, children12, 1200, True) ##CHILL
 onode_11 = opNode(11, children11, 60, False)  ##COMBINE
 onode_10 = opNode(10, children10, 2400, True)  ##REFRIGERATE
 onode_9 = opNode(9, children9, 60, False)  ##mix in bowl
 onode_8 = opNode(8, children8, 3000, True)  ##Bake
 onode_7 = opNode(7, children7, 30, False)  ##create gelatin
 onode_6 = opNode(6, children6, 600, True)  ##preheat oven
 onode_5 = opNode(5, children5, 10, False)  ##mix in pan
 onode_4 = opNode(4, children4, 300, True)  ##boil in water
 onode_3 = opNode(3, children3, 20, False)  ##turn on oven
 onode_2 = opNode(2, children2, 20, False)  ##melt butter
 onode_1 = opNode(1, children1, 30, False)  ##pour water

 recipeNode4.add_child(onode_12)
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

 opSeq(recipeNode1)
 print(" ")
 opSeq(recipeNode2)
 print(" ")
 opSeq(recipeNode3)
 print(" ")
 opSeq(recipeNode4)
 print(" ")