import P3.i_node


class Heater():

    """
    Heater class:   Represents the heater in the Rankine cycle
    """

    def __init__(self,name,inletNode,exitNode,I_inletNode,I_exitNode):
        """
        Initializes the heater with nodes
        """
        self.inletNode = inletNode
        self.exitNode = exitNode
        self.I_inletNode = I_inletNode
        self.I_exitNode = I_exitNode
        self.m = 1
        self.y_ = None
        self.name=name
        
        
    def state(self,nodes):
        nodes[self.exitNode].p = nodes[self.inletNode].p
        nodes[self.I_inletNode].p = nodes[self.I_exitNode].p
        nodes

        nodes[self.I_exitNode].ps()
        nodes[self.I_inletNode].ps()
        nodes[self.inletNode].ps()
        nodes[self.exitNode].ps()

   
    def simulate(self,nodes):
        """
        Simulates the heater 
        """
        
        self.y_ = (nodes[self.I_exitNode].h - nodes[self.I_inletNode].h)/(nodes[self.inletNode].h-nodes[self.exitNode].h)
        
    '''
        self.Y2=(nodes[self.O_WexitNode].h - nodes[self.O_WinletNode].h + self.Y1* \
        (nodes[self.O_WinletNode].h - nodes[self.O_AexitNode].h ))/ \
        (nodes[self.O_AinletNode].h - nodes[self.O_WinletNode].h)    
           
    '''   
    def mdotenergy(self,mdot):
        pass 
    