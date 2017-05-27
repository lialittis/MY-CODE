import P3.i_node

class Condenser(object):
    """
    The condenser class
    """

    def __init__(self, name, inletNode, exitNode):
        """
        Initializes the condenser with nodes
        """
        self.inletNode = inletNode
        self.exitNode = exitNode
        self.name = name
        self.m = 1
        self.y_ = 0
        self.y__ = 0
        

    def state(self, nodes):
        nodes[self.exitNode].x = 0
        nodes[self.inletNode].p = nodes[self.exitNode].p
        if nodes[self.exitNode].p != None and nodes[self.exitNode].x != None:
            nodes[self.exitNode].px()

    def simulate(self, nodes):
        
        self.heatExtracted = (self.m-self.y_-self.y__)*(nodes[self.inletNode].h - nodes[self.exitNode].h)
        nodes[self.inletNode].m=nodes[self.exitNode].m
        """
        Question:self.m = 1?
        
        """
        
    def mdotenergy(self, mdot):
        self.Qoutdot = mdot * self.heatExtracted / (3600 * 1000)
        
'''
    def cw_nodes(self, inletNodeW, exitNodeW):
        self.inletNodeW = inletNodeW
        self.exitNodeW = exitNodeW

    def cw_simulate(self, nodew):
        """
        Simulates the Condenser 
        """
        self.mcwdot = (self.Qoutdot * 1000 * 3600) / \
            (nodew[self.exitNodeW].h - nodew[self.inletNodeW].h)
'''