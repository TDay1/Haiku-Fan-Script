"""
V 1.0
This is a script written by Tom Day in python 2.7 that controls Haiku smart fans connected to a network.
This script ecxploits the fact that the fans are controlled using unencrypted traffic over the network.

To run on linux: python haiku.py
"""

import socket
import os
import sys

def clear(numlines):
    print('\n' * numlines)

def IHatePython(UDP_IP, UDP_PORT):
#get speed to set the fan at
    SPEED = raw_input ("Enter the fan's speed (0-7): ")
#create message to send to fan
    M1 = "<ALL;FAN;SPD;SET;"
    M3 = ">"
    MESSAGE = M1 + SPEED + M3

#Echo packet infomation to user
    print "Setting fan on", UDP_IP, "to speed:", SPEED
    print "UDP target port:", UDP_PORT
    print "message:", MESSAGE

#create packet
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
#Ask if user would like to run script again
    question = "Would you like to run the script again?"
    while "the answer is invalid":
         reply = str(raw_input(question+' (y/n): ')).lower().strip()
         if reply[0] == 'y' or 'yes':
            clear(100)
            IHatePython(UDP_IP, UDP_PORT)
         if reply[0] == 'n':
            clear(100)
            print "Goodbye!"
            sys.exit()

#clear screen
clear(100)
#get the fan's ip (Default: 192.168.1.1)
UDP_IP = raw_input("Enter the fan's ip (Enter for default): ") or "192.168.1.1"
#get the fan's open port (Deafault: 31415)
UDP_PORT = raw_input("Enter the fan's port (Enter for default): ") or 31415
IHatePython(UDP_IP, UDP_PORT)
