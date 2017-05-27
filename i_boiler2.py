import P3.i_node

class Boiler2(object):
    """
    The boiler class
    """

    def __init__(self, name, inletNode, exitNode):
        """
        Initializes the boiler 
        """
        self.inletNode = inletNode
        self.exitNode = exitNode
        self.name = name
        self.m = 1
        self.y_ = None
    
    def state(self, nodes):
        
        nodes[self.inletNode].p = nodes[self.exitNode].p
        
        if nodes[self.exitNode].p!= None and nodes[self.exitNode].t!= None:
            nodes[self.exitNode].pt()

    def simulate(self, nodes):
        
            self.heatAdded = (self.m-self.y_)*(nodes[self.exitNode].h - nodes[self.inletNode].h)

    def mdotenergy(self, mdot):
        self.Qindot = mdot * self.heatAdded / (3600 * 1000)
