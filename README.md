# Haiku-Fan-Script
This is a python script that can be used to control Haiku Fans over networks.

## How does it work?
This is a script that exploits the fact that Haiku fans are controlled using unencrypted UDP packets by simply recreating one of the packets with certain infomation and sending it to the fan in question. As of now all this script does is turn on and off the fan and set it's speed but in future (When I get time) I will add support for lights.

## How to use
On linux just run python Haiku.py

## Why did I make this
I share a network with some people who installed these fans and I want to mess with them.
