import sys

# OpNode Class
# An OpNode can be a recipe, ingredient, or task
# idx: Each opNode has a unique integer id. Ex: Boiling water will always be 1
#
# children: The children are the dependencies, tasks that must be completed for the
# task to execute. For ingredients, this will always be empty and for 
# recipes, this should never be empty
#
# duration: is the amount of time for a task to exectue. For recipes and ingredients
# this should default to -1
#
# involvement: This is true for passive tasks, and false for anything else

class opNode:
    def __init__(self, idx, children, resources):
        self.idx = idx
        self.children = []
        self.resources = resources
        self.cpl = 0
        self.reached = False
        self.completed = False


# Helper functions for debugging
    def status(self):
        status = dict()
        status['id'] = self.idx
        status['resources'] = self.resources
        status['childen'] = [d.idx for d in self.children]
        return status

    def display(self):
        print(self.status())

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)
            return True
        return False


