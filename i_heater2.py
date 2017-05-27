
import P3.i_node

class Heater2():

    """
    Heater2 class:   Represents another heater in the Rankine cycle
    """

    def __init__(self, name,inletNode_1,inletNode_2,inletNode_3,exitNode):
        """
        Initializes the heater with nodes
        """
        self.inletNode_1 = inletNode_1
        self.exitNode = exitNode
        self.inletNode_2 = inletNode_2
        self.inletNode_3 = inletNode_3
        self.m = 1
        self.y_ = None
        self.y__ = None
        self.name=name
        

    def state(self,nodes):
        nodes[self.inletNode_1].p = nodes[self.inletNode_2].p = \
        nodes[self.inletNode_3].p = nodes[self.exitNode].p
    
    
    def simulate(self,nodes):
        if self.y_!= None:
            self.y__=(nodes[self.exitNode].h - nodes[self.inletNode_2].h + self.y_* \
            (nodes[self.inletNode_3].h - nodes[self.inletNode_2].h ))/ \
            (nodes[self.inletNode_1].h - nodes[self.inletNode_2].h)    
                 
        """
        Simulates the heater 
        """

    def mdotenergy(self,mdot):
        pass
