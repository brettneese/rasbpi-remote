#!/usr/bin/env python
from scapy.all import *
import lircplayback as playback

def button_pressed():
    playback.airplay_toggle()


def arp_display(pkt):
    if pkt[ARP].op == 1: #who-has (request)
        if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
            if pkt[ARP].hwsrc == '74:c2:46:a8:db:b6': # Huggies
                button_pressed()

sniff(prn=arp_display, filter="arp", store=0)
