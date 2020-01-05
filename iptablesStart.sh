#!/bin/bash
# Firewall apps - only allow apps run from "internet" group to run

# clear previous rules
sudo iptables -F

sudo iptables -A FORWARD -i 192.168.137.225 -p tcp --dport 53 -j ACCEPT

sudo iptables -A FORWARD -i wlan0 -p udp --dport 53 -j ACCEPT

sudo iptables -A FORWARD -i wlan0 -p tcp --dport 80 -d 192.168.137.15 -j ACCEPT
