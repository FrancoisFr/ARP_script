#!/usr/bin/python
"""
Custom topology example
One directly connected switch plus three host attached to the switch with a controller 
(c0) and an additional external interface connected to s1
"""

from mininet.net import Mininet
from mininet.link import Intf
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.topo import SingleSwitchTopo
# OpenDayLight controller
FL_CONTROLLER_IP='172.16.0.23'
FL_CONTROLLER_PORT=6653
# Define remote OpenDaylight Controller
info( 'Floodlight IP Addr:', FL_CONTROLLER_IP, '\n' )
info( 'Floodlight Port:', FL_CONTROLLER_PORT, '\n' )
def customNet():
    "Create a customNet and add devices to it."
    net = Mininet( topo=None, build=False )
    # Add controller
    info( 'Adding controller\n' )
    net.addController( 'c0', 
                       controller=RemoteController, 
                       ip=FL_CONTROLLER_IP, 
                       port=FL_CONTROLLER_PORT 
                     )
    # Add physical interface
    info( 'Defining physical interface\n' )
    intfName = 'enp0s8'
    
    # Add hosts 
    info( 'Adding hosts\n' )
    h1 = net.addHost( 'h1' )
    h2 = net.addHost( 'h2' )
    h3 = net.addHost( 'h3' )
    # Add switches
    info( 'Adding switches\n' )
    s1 = net.addSwitch( 's1' )
    # Add links
    info( 'Adding host links\n' )
    net.addLink( h1, s1 )
    net.addLink( h2, s1 )
    net.addLink( h3, s1 )
    info( 'Adding hardware interface', intfName, 'to switch', s1.name, '\n' )
    _intf = Intf( intfName, node=s1 )
    
    info( '*** Starting network ***\n')
    net.start()
    info( '*** Running CLI ***\n' )
    CLI( net )
    info( '*** Stopping network ***' )
    net.stop()
if __name__ == '__main__':
    setLogLevel( 'info' )
    customNet()
