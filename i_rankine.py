'''
Step by step codes of the ideal rankine cycle simulator to demonstrate: 

    Data Structures+ Algorithms = Programs


'''
from tabulate import tabulate
import csv

import P3.i_node
import P3.i_turbine
import P3.i_turbine2
import P3.i_pump
import P3.i_pump2
import P3.i_condenser
import P3.i_boiler
import P3.i_heater
import P3.i_heater2
import P3.i_trap


def read_nodesfile(filename):
    """ get nodes in the  csv file"""
    countNodes = len(open(filename, 'r').readlines()) - 1
    nodes = [None for i in range(countNodes)]
    csvfile = open(filename, 'r')
    reader = csv.DictReader(csvfile)
    for line in reader:
        i = int(line['NID'])
        nodes[i] = P3.i_node.Node(line['NAME'], i)
        try:
            nodes[i].p = float(line['p'])
        except:
            nodes[i].p = None
        try:
            nodes[i].t = float(line['t'])
        except:
            nodes[i].t = None
        try:
            nodes[i].x = float(line['x'])
        except:
            nodes[i].x = None
        
        
        if line['p'] != '' and line['t'] != '':
            nodes[i].pt()
        elif line['p'] != '' and line['x'] != '':
            nodes[i].px()
        elif line['t'] != '' and line['x'] != '':
            nodes[i].tx()
        
        """
        
        The h,s,t,x of nodes[i] can be gotten at other classes.
        
        """
        
    return nodes, countNodes


def read_devicefile(filename):
    devFile = open(filename, 'r')
    #discardHeader = devFile.readline()
    Comps = {}
    i = 0
    begId = 2
    
    tur = []
    tur2 = []
    bo = []
    con = []
    pu = []
    pu2 = []
    oph = []
    clh = []
    tr = []
    
    for line in devFile:
        dev = line.split(',')
        if dev[1] == "TURBINE1":
            tur.append(P3.i_turbine.Turbine(dev[0], int(dev[begId]), int(dev[begId + 1]), int(dev[begId + 2])))
        elif dev[1] == "TURBINE2":
            tur2.append(P3.i_turbine2.Turbine2(dev[0],int(dev[begId]),int(dev[begId + 1]),int(dev[begId + 2]))) 
        elif dev[1] == "BOILER":
            bo.append(P3.i_boiler.Boiler(dev[0], int(dev[begId]), int(dev[begId + 1])))
        elif dev[1] == "CONDENSER":
            con.append(P3.i_condenser.Condenser(dev[0], int(dev[begId]), int(dev[begId + 1])))
        elif dev[1] == "PUMP":
            pu.append(P3.i_pump.Pump(dev[0], int(dev[begId]), int(dev[begId + 1])))
        elif dev[1] == "PUMP2":
            pu2.append(P3.i_pump2.Pump2(dev[0], int(dev[begId]), int(dev[begId + 1])))
        elif dev[1] == "OPENHEATER":
            oph.append(P3.i_heater.Heater(
                dev[0], int(dev[begId]),int(dev[begId + 1]), int(dev[begId + 2]), int(dev[begId + 3])))
        elif dev[1] == "CLOSEDHEATER":
            clh.append(P3.i_heater2.Heater2(
                dev[0], int(dev[begId]),int(dev[begId + 1]), int(dev[begId + 2]), int(dev[begId + 3])))   
        elif dev[1] == "TRAP":
            tr.append(P3.i_trap.Trap(dev[0], int(dev[begId]),int(dev[begId + 1])))        
        i = i + 1
        """
        i is the number of devices.
        """ 
    DevNum = i
    
    Comps["TURBINE"] = tur
    Comps["TURBINE2"] = tur2
    Comps["BOILER"] = bo
    Comps["CONDENSER"] = con
    Comps["PUMP"] = pu
    Comps["PUMP2"] = pu2
    Comps["OPENHEATER"] = oph 
    Comps["CLOSEDHEATER"] = clh
    Comps["TRAP"] = tr   
    return Comps , DevNum

"""
"""

class RankineCycle(object):

    def __init__(self, name, nodefilename, devfilename):
        
        self.name = name
        self.nodes = []
        self.devs = {}
        self.nodes, self.NodeNum = read_nodesfile(nodefilename)
        self.devs,self.DevNum = read_devicefile(devfilename)

    def state(self):
        
        for i in range(len(self.nodes)):
            if self.nodes[i].p != None and self.nodes[i].t != None:
                self.nodes[i].pt()
            elif self.nodes[i].p != None and self.nodes[i].x != None:
                self.nodes[i].px()
            elif self.nodes[i].t != None and self.nodes[i].x != None:
                self.nodes[i].tx()
            elif self.nodes[i].h != None and self.nodes[i].s !=  None:
                self.nodes[i].hs()
            elif self.nodes[i].p != None and self.nodes[i].h !=  None:
                self.nodes[i].ph()
            elif self.nodes[i].p != None and self.nodes[i].s !=  None:
                self.nodes[i].ps()
            
            # After the maxium trials, all the states should be known
            
            for key in self.devs:
                for i in range(len(self.devs[key])):
                    self.devs[key][i].state(self.nodes)

            
            """
            make self.nodes more complicated
            
            """    
                
        
    def simulate(self):
        
        self.workExtracted = 0
        self.heatAdded = 0   
        self.workRequired = 0


        for key in self.devs:
            for i in range(len(self.devs[key])):
                self.devs[key][i].simulate(self.nodes)            

        for i in range(len(self.devs["BOILER"])):
            self.heatAdded = self.heatAdded +  self.devs["BOILER"][i].heatAdded
            
        for i in range(len(self.devs["TURBINE"])):
            self.workExtracted = self.workExtracted + self.devs["TURBINE"][i].Extracth
        for i in range(len(self.devs["TURBINE2"])):
            self.workExtracted = self.workExtracted + self.devs["TURBINE2"][i].Extracth
        
                               
        for i in range(len(self.devs["PUMP"])):
            self.workRequired = self.workRequired + self.devs["PUMP"][i].Needh
        for i in range(len(self.devs["PUMP2"])):
            self.workRequired = self.workRequired + self.devs["PUMP2"][i].Needh
            
        self.bwr = self.workRequired/self.workExtracted
        self.efficiency = (self.workExtracted - self.workRequired) / (self.heatAdded)


        
    def spower_simulate(self, Wcycledot):
        self.Wcycledot = Wcycledot
        self.mdot = Wcycledot * 1000.0 * 3600.0 / (self.workExtracted -self.workRequired)
        
        
        for key in self.devs:
            for i in range(len(self.devs[key])):
                self.devs[key][i].mdotenergy(self.mdot)                  
        


    def export(self):
        table1 = []
        
        for i in range(self.NodeNum):
            table1.append(self.nodes[i].printnodes())
        headers =  ['No.', 'Name', 'Pressure  Mpa', 'Temperature  °C', 'Enthalpy  kJ/kg', 'Etropy  kJ/(kg*K)', 'Bypass coefficient']
        
        print(" \n --------  %s   ----------------------------------" % self.name)
        """
        print("The net power output: ", self.Wcycledot, "MW")
        print("Efficiency: ", '%.2f' % (self.efficiency * 100), "%")
        print("The back work ratio: ", '%.2f' % (self.bwr * 100), "%")
        print("The mass flow rate: ", '%.2f' % self.mdot, "kg/h")
        print('The rate of heat transfer as the fluid passes the boiler: ',
              '%.2f' % self.devs['Boiler'].Qindot, 'MW')
        print(" \n -------  Circulating Water System  --------------")
        print("Cooling water enters the condenser T:", self.nodew[0].t, u'°C')
        print("Cooling water exits  the condenser T:", self.nodew[1].t, u'°C')
        print('The rate of heat transfer from the condensing steam: ',
              '%.2f' % self.devs['Condenser'].Qoutdot, 'MW')
        print('The mass flow rate of the condenser cooling water: ', '%.2f' %
              self.devs['Condenser'].mcwdot, 'kg/h')
        print(" \n -------- NODES  -----------------------------------")
        print("\nNodeID\tName\tP\tT\tH\tS\tV\tX")
        for inode in self.nodes:
            print(inode)
        """
        print(tabulate(table1,headers), '\n')
        print("The net power output of the cycle: ", self.Wcycledot, "MW")
        print("Efficiency: ", '%.2f' % (self.efficiency * 100), "%")
        print("The mass flow rate: ",  '%.2f' % self.mdot, "kg/h")


if __name__ == '__main__':
    nds_filename = 'rankine86-nds.csv'
    dev_filename = 'rankine86-dev.csv'
    
    c86 = RankineCycle("Rankine86", nds_filename,  dev_filename)
    
    c86.state()
    c86.simulate()
    # Specified Net Output Power
    Wcycledot = 100
    c86.spower_simulate(Wcycledot)
    #c81.cw_simulate()
    c86.export()