import P3.i_node

class Boiler:
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
        self.y_ = 0
    
    def state(self, nodes):
        
        nodes[self.inletNode].p = nodes[self.exitNode].p
        
        if nodes[self.exitNode].p!= None and nodes[self.exitNode].t!= None:
            nodes[self.exitNode].pt()
        if nodes[self.inletNode].p!=None and nodes[self.inletNode].t!=None:
            nodes[self.inletNode].pt()

    def simulate(self, nodes):
        
        self.heatAdded = (self.m-self.y_)*(nodes[self.exitNode].h - nodes[self.inletNode].h)

    def mdotenergy(self, mdot):
        self.Qindot = mdot * self.heatAdded / (3600 * 1000)
