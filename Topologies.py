from mininet.topo import Topo


# List of Hosts
h=[]

# List of Switches
sw=[]


#---------------------------------------------------------
                        ### Topology 1 
#---------------------------------------------------------


class MyTopo_1( Topo ):

    def __init__( self ):

        # Initialize topology
        Topo.__init__( self )

        # Add Hosts
        for i in range (0,6):
            h.append(self.addHost('h%s' % (i)))

        # Add Switches 
        for i in range (0,2):
            sw.append(self.addSwitch('sw%s' % (i)))

        # Add Links between Hosts and Switches
        for i in range (0,6):
            if i<3 :
                self.addLink(h[i], sw[0])

            else:
                self.addLink(h[i], sw[1])
	
	# Add Link between Switches      
        self.addLink( sw[0], sw[1] )
        

#---------------------------------------------------------
			### Topology 2 
#---------------------------------------------------------


class MyTopo_2( Topo ):

    def __init__( self ):

        # Initialize topology
        Topo.__init__( self )

        # Add Hosts
        for i in range (0,12):
            h.append(self.addHost('h%s' % (i)))


        # Add Switches 
        for i in range (0,6):
            sw.append(self.addSwitch('sw%s' % (i)))


        # Add Links between Switches and Hosts
        for i in range (0,12):
            if i<3 :
                self.addLink(h[i], sw[2])

            if 2< i <6:
                self.addLink(h[i], sw[3])

            if 5< i <9:
                self.addLink(h[i], sw[4])

            if 8< i <12:
                self.addLink(h[i], sw[5])


	# Add links between switches
        self.addLink( sw[0], sw[1] )
        self.addLink( sw[0], sw[2] )
        self.addLink( sw[0], sw[3] )
        self.addLink( sw[1], sw[4] )
        self.addLink( sw[1], sw[5] )


#---------------------------------------------------------
                        ### Topology 3 
#---------------------------------------------------------


class MyTopo_3( Topo ):

    def __init__( self ):

        # Initialize topology
        Topo.__init__( self )

        # Add Hosts
        for i in range (0,12):
            h.append(self.addHost('h%s' % (i)))


        # Add Switches 
        for i in range (0,6):
            sw.append(self.addSwitch('sw%s' % (i)))


        # Add Links between Switches and Hosts       
        for i in range (0,12):
            if i<3 :
                self.addLink(h[i], sw[2])

            if 2< i <6:
                self.addLink(h[i], sw[3])

            if 5< i <9:
                self.addLink(h[i], sw[4])

            if 8< i <12:
                self.addLink(h[i], sw[5])

	# Add Links between Switches
	j=0
	while j<2:
	    for i in range (2,6):
                self.addLink(sw[i], sw[j])
            j+=1

# Dictionary with topologies
topos = {'mytopo_1': ( lambda: MyTopo_1() ),'mytopo_2': ( lambda: MyTopo_2() ), 'mytopo_3': ( lambda: MyTopo_3() ) }

