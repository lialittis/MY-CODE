import P3.i_node

class Turbine():

    """
    Turbine class:   Represents a turbine in the Rankine cycle
    """

    def __init__(self, name,inletNode,outletNode,exitNode):
        """
        Initializes the turbine with nodes
        """
        self.inletNode = inletNode
        self.exitNode=exitNode
        self.outletNode=outletNode
        self.name=name
        self.m=1
        self.y_= None

    def state(self,nodes):
        
        nodes[self.inletNode].s = nodes[self.outletNode].s = nodes[self.exitNode].s

        nodes[self.exitNode].ps()
        nodes[self.outletNode].ps()

 
    def simulate(self,nodes):
        """
        Simulates the turbine 
        """
                
    
        if self.y_!= None:
            self.workExtracted = (self.m*(nodes[self.inletNode].h - nodes[self.outletNode].h) \
                         + (self.m - self.y_)*(nodes[self.outletNode].h - nodes[self.exitNode].h))
    def mdotenergy(self,mdot):
        
        self.WExtracted=mdot* self.workExtracted 
        