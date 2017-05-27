import P3.i_node

class Pump2():

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

    
    def state(self,nodes):
        nodes[self.exitNode].s = nodes[self.inletNode].s
        nodes[self.exitNode].h=nodes[self.inletNode].h\
                               +nodes[self.inletNode].v*(nodes[self.exitNode].p \
                               -nodes[self.inletNode].p)*1000
        nodes[self.exitNode].hs()     

    def simulate(self,nodes):
        
        """
        Simulates the pump 
        """

        self.workRequired =nodes[self.exitNode].h - nodes[self.inletNode].h
    
    def mdotenergy(self,mdot):
        self.WRequired=mdot* self.workRequired 