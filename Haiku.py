"""
V 1.0
This is a script written by Tom Day in python 2.7 that controls Haiku smart fans connected to a network.
This script exploits the fact that the fans are controlled using unencrypted traffic over the network.

To run on linux: python haiku.py
"""

import socket
import os
import sys

def clear(numlines):
    print('\n' * numlines)

def main(UDP_IP, UDP_PORT):
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
    if yes_no("Would you like to run the script again (y/n)") == True:
		clear(100)
            	main(UDP_IP, UDP_PORT)
    else:
            clear(100)
            print "Goodbye!"
            sys.exit()

def yes_no(answer):
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])
    
    while True:
        choice = raw_input(answer).lower()
        if choice in yes:
           return True
        elif choice in no:
           return False
        else:
           print "Please respond with 'yes' or 'no'\n"

#clear screen
clear(100)
#get the fan's ip (Default: 192.168.1.1)
UDP_IP = raw_input("Enter the fan's ip (Enter for default): ") or "192.168.1.1"
#get the fan's open port (Deafault: 31415)
UDP_PORT = raw_input("Enter the fan's port (Enter for default): ") or 31415
main(UDP_IP, UDP_PORT)
