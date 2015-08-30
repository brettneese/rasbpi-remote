#!/usr/bin/env python
from scapy.all import *
import lircplayback as playback
import signal

def button_pressed():
    playback.airplay_toggle()


def arp_display(pkt):
    if pkt[ARP].op == 1: #who-has (request)
        if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
            if pkt[ARP].hwsrc == '74:c2:46:a8:db:b6': # Gatorade button
                button_pressed()

sniff(prn=arp_display, filter="arp", store=0)

def sigterm_handler(_signo, _stack_frame):
    "When sysvinit sends the TERM signal, cleanup before exiting."
    print("[" + get_now() + "] received signal {}, exiting...".format(_signo))
    cleanup_pins()
    sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)
