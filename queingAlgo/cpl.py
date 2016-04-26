from Graph import Graph
from opNode import opNode



class IterableQueue():
    def __init__(self,source_queue):
            self.source_queue = source_queue
    def __iter__(self):
    	while True:
            try:
               yield self.source_queue.get_nowait()
            except Queue.Empty:
               return

def getCPL(opNode):
	return opNode.cpl

def calcCPLs(graph, recipeNode):
	bag = set()
	while(recipeNode.reached != True):
		for key in graph.graph_dict:
			if (graph.graph_dict[key] == []):
				key.reached = True
			else:
				key.reached = True
				for c in graph.graph_dict[key]:
					if c.reached == False:
						key.reached = False
			if key.reached == True:
				#print("just reached " + str(key.idx))
				maxcpl = 0
				for c in key.children:
					if(c.cpl > maxcpl):
						maxcpl = c.cpl
				if(key.involvement == True):
					key.cpl = key.duration + maxcpl
					#print("checkpoint")
				else:
					key.cpl = maxcpl

			bag.add(key)
	return bag

def schedule(l, recipeNode):
	order = []
	while(recipeNode.completed != True):
		for n in l:
			if n.completed == False:
				if reachable(n):
					n.completed = True
					order.append(n)
	return order

def reachable(node):
	for c in node.children:
		if c.completed == False:
			return False
	return True

if __name__ == "__main__":

 children1 = Set([]) 
 children2 = Set([])
 children3 = Set([])
 children4 = Set([])
 children5 = Set([])


 recipeNode = opNode(5, children5, 15, False) 
 onode_1 = opNode(1, children1, 10, False)
 onode_2 = opNode(2, children2, 10, False)
 onode_3 = opNode(3, children3, 5, True)
 onode_4 = opNode(4, children4, 20, False)
	

 recipeNode.add_child(onode_2)
 recipeNode.add_child(onode_4)
 onode_4.add_child(onode_3)
 onode_4.add_child(onode_1)


 graph = genGraph(recipeNode)

 result =(calcCPLs(graph, recipeNode))

 l = list(sorted(result, key=getCPL, reverse=True))


 optimalOrder = schedule(l, recipeNode)

 for s in optimalOrder:
 	print("node: " + str(s.idx) + "cpl: " + str(s.cpl))
