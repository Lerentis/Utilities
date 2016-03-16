# networkingUtilities
Some utilities to detect and interact with an unknown network

## What it is

This is a collection of some helpful tools to administrate a network, which you have not planed yourself.
This collection includes:

* subnet detection
* subnet scanner
* WOL
* ssh
* traceroute 

## What it is not

A tool with just click and go. As in the current state you have to modify the main.py to your needs.

# Requirements:

* python 3
* python wakeonlan (well... for wake on lan?)
* python nmap (for scanning)
* python paramiko (for ssh)
* python scapy3 (for traceroute)