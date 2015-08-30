#!/usr/bin/env python

import pyshark
import config
import os
import lircplayback as playback
import signal


def airplay_callback(pkt):
    try:
        print pkt
        if pkt.rtsp.Method == "RECORD":
            print "PLAYBACK STARTED"
            playback.airplay_toggle()

        if pkt.rtsp.Method == "TEARDOWN":
            print "PLAYBACK STOPPED"
            playback.airplay_toggle()

    except:
        pass
# meh

# this is a dumb thing to do
os.system('sudo service ifplugd stop; sudo ifconfig ' + config.wireless_card + ' down; sudo iwconfig ' + config.wireless_card + ' mode monitor; sudo ifconfig ' + config.wireless_card + ' up')

capture = pyshark.LiveCapture(config.wireless_card, display_filter='tcp.port eq 5000 or eapol or tcp.port eq 7000', decode_as={"tcp.port==5000": 'rtsp'}, decryption_key=config.decryption_key, encryption_type=config.encryption_type)

capture.set_debug()
capture.apply_on_packets(airplay_callback)

def sigterm_handler(_signo, _stack_frame):
    "When sysvinit sends the TERM signal, cleanup before exiting."
    print("[" + get_now() + "] received signal {}, exiting...".format(_signo))
    cleanup_pins()
    sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)


# Define the MAC of your Airplay Receiver here, to prevent intercepting non-AirPlay packets (also useful if you have multiple airplay clients)
# airplayDestMAC = config.airplayDestMAC
