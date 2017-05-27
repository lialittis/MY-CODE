import P3.i_node


class Trap():
    '''
    The trap class
    '''
    def __init__(self, name, inletNode, exitNode):
        self.inletNode = inletNode
        self.exitNode = exitNode
        self.name=name
        self.m = 1
       
    def state(self, nodes): 
        nodes[self.inletNode].h = nodes[self.exitNode].h
        #nodes[self.exitNode].ph() 
                
        
    def simulate(self, nodes):
        pass
    
    def mdotenergy(self,mdot):
        pass
    