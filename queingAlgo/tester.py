'''
Test Querying from the Parse Database

Instructions: Put the name of the TaskNode
you are looking for on line 33, 
pulled_node = db_caller.create_tasknode('NAME HERE')

if that tasknode exists in the database, you will
get a recursive list of it and its dependencies
and their dependencies, and so on.

if that tasknode does not exist in the database,
you will get a message:

"Could not find the specified tasknode"

'''

from databasecaller import DatabaseCaller
from databasecaller import Recipe as rp
from TaskNode import TaskNode

# from algo.TnodeUtils import printTasks
from algo2.opSeq import opSeq
from algo2.opNode import opNode

#print the status (and the status of its dependencies,
#and their dependencies recursively)
#for a given tasknode
def printStatus(tasknode, list_of_tasks):
    #tasknode.display()        #COMMENTED OUT
    list_of_tasks.append(tasknode)
    for i in tasknode.dependencies:
        printStatus(i, list_of_tasks)
        #tnode = TaskNode(i.name, i.short_descr, i.long_descr, i.time)
        
target_name = "ramen"

def main():
    # This section recursively creates a list of tasknodes
    list_of_tasks = []
    db_caller = DatabaseCaller()
    pulled_node = db_caller.create_tasknode(target_name)
    if (pulled_node is None):
        pass
    else:
        printStatus(pulled_node, list_of_tasks)

    # Iterate through list and give some attributes similar to opNode
    my_dict = {}
    for i in range(len(list_of_tasks)):
        list_of_tasks[i].idx = i
        # use a dictionary to map name dependencies to numbers
        my_dict[list_of_tasks[i].name] = i
        list_of_tasks[i].involvement = not list_of_tasks[i].flags['active']
        #print(list_of_tasks[i])

    # Adds a list of numbers, namely children to each task node
    for k in list_of_tasks:
        children = []
        for h in k.dependencies:
            #print(k.name + " depends on " + h.name)
            children.append(my_dict[h.name])
        k.children = children
        #print(k.name + " has - ")
        #print(k.children)

    # goes through and converts all tasknodes to recipe nodes
    list_of_opnodes = []
    recipe_node = opNode(0, list_of_opnodes, 0, True)
    for j in list_of_tasks:
        print("j.name: " + j.name)
        if j.name != target_name:
            list_of_opnodes.append(opNode(j.idx, j.children, j.time, j.involvement))
        else:
            print("found target")
            recipe_node = opNode(j.idx, j.children, j.time, j.involvement)
            list_of_opnodes.append(recipe_node)
            print(j.children)
            print(recipe_node.children)

    # converts the numeric children to reference children
    for k in range(len(list_of_tasks)):
        for h in list_of_tasks[k].children:
            list_of_opnodes[k].add_child(list_of_opnodes[h])

        #print(j.name)
    print(list_of_opnodes[1].idx)
    print(list_of_opnodes[1].children)
    opSeq(recipe_node)
        #list_of_tasks.append(pulled_node)
    # list_of_tasks = db_caller.my_set
    # print(db_caller.my_set)
    # for i in list_of_tasks:
    #     print(i)
    # core_engine = CE(list_of_tasks)
    # core_engine.printTasks()

if __name__ == '__main__':
   main()