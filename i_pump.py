import P3.i_node

class Pump():

    """
    Pump class： Represents a pump in the Rankine cycle
    """

    def __init__(self,name,inletNode, exitNode):
        
        """
        Initializes the pump with nodes
        """
        
        self.inletNode = inletNode
        self.exitNode = exitNode
        self.name=name
        self.m = 1
        self.y_=None
        self.y__= None
    
    def state(self,nodes):
        nodes[self.exitNode].s = nodes[self.inletNode].s
        #nodes[self.exitNode].h = nodes[self.inletNode].h + nodes[self.inletNode].v*(nodes[self.exitNode].p - nodes[self.inletNode].p)*1000
        #nodes[self.exitNode].hs()     

    def simulate(self,nodes):
        
        """
        Simulates the pump 
        """
        
        """
        if self.y_!= None:
            self.y__=(nodes[self.exitNode].h - nodes[self.inletNode_2].h + self.y_* \
            (nodes[self.inletNode_3].h - nodes[self.inletNode_2].h ))/ \
            (nodes[self.inletNode_1].h - nodes[self.inletNode_2].h)    
        
        """
        if self.y_!=None and self.y__!=None:
            self.workRequired =(1-self.y_-self.y__)*( nodes[self.exitNode].h - nodes[self.inletNode].h)
    
    def mdotenergy(self,mdot):
        self.WRequired=mdot* self.workRequired 