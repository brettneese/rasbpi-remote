# rasbpi-remote 

Scripts for controlling a home theate system using contextual (network) actions.

Used primarily on a Raspberry Pi to control an IR transmitter that automatically powers an home theatre receiver on and off based on AirPlay traffic, may add more stuff later. Video demo: https://www.youtube.com/watch?v=Xe2hQXnwOaE

# Requirements

- Python 2.7
- WireShark
- The forked version of PyShark in the repo (haven't had a chance to post fixes back to PyShark)

# Design Philosophy

airplay-listener, dash-listener, and remote-web are seperate modules even though they share a repo, and should be thought of as interfaces around the core module, lirc-playback, which is fundamentally an SDK/API around the appopriate LIRC commands being run on the shell. 

Thereotically there could be more interfaces and more listeners that triger actions but it's better to build them seperately vs cramming everything into one giant module. 

# Installation Instructions
sudo pip install 

move config.py from /dist/ to airplay-listener 

move init scripts to init.d (or however you prefer to run things on startup)

# N.B. 

I know this is horribly built. Working on removing the dependencies on sudoing all over everywhere and on using os.system. Some parts currently need to be run as sudo, so tread lightly. 

Good documentation on the AirPlay protocol can be found: 

- http://git.zx2c4.com/Airtunes2/about/ 
- http://nto.github.io/AirPlay.html

Make sure your wifi card is running in monitor mode and that you're using a decent wifi card. There's now some initalization code to make that happen. I use this http://www.amazon.com/dp/B002SZEOLG/ref=sr_ph_1?m=ATVPDKIKX0DER&ie=UTF8&qid=1440124668&sr=sr-1&keywords=tplink+high+gain on my Pi and it works really well.

WPA/WPA2 decryption *should* work out of the box (once you configure Wireshark, as tshark uses Wireshark's configuration profile), but it's finnicky. 
