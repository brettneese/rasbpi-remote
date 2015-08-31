#!/usr/bin/env python
from scapy.all import *
import lircplayback as playback
import signal


def button_pressed():
    print "button pressed"
    playback.tuner_toggle(50)


def arp_display(pkt):
    try:
        if pkt[ARP].op == 1:
            if pkt[ARP].psrc == '0.0.0.0':
                if pkt[ARP].hwsrc == '74:c2:46:a8:db:b6':
                    button_pressed()
                else:
                    print "ARP Probe from unknown device: " + pkt[ARP].hwsrc
    except IndexError:
        pass
print sniff(prn=arp_display, filter="arp", store=0)


def sigterm_handler(_signo, _stack_frame):
    "When sysvinit sends the TERM signal, cleanup before exiting."
    print("[" + get_now() + "] received signal {}, exiting...".format(_signo))
    cleanup_pins()
    sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)
