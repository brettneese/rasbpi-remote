# airplay-monitor 

Scripts for monitoring the status of an AirPlay receiver.

Used primarily on a Raspberry Pi to control an IR transmitter that automatically powers an home theatre receiver on and off, may add more stuff later. Video demo: https://www.youtube.com/watch?v=Xe2hQXnwOaE

# Requirements

- Python 2
- WireShark
- The forked version of PyShark in the repo (haven't had a chance to post fixes back to PyShark)

# N.B. 

I know this is horribly built. Working on removing the dependencies on sudoing all over everywhere and on using os.system. Currently needs to be run as sudo, so tread lightly. 

Good documentation on the AirPlay protocol can be found: 

- http://git.zx2c4.com/Airtunes2/about/ 
- http://nto.github.io/AirPlay.html

Make sure your wifi card is running in monitor mode and that you're using a decent wifi card. There's now some initalization code to make that happen. I use this http://www.amazon.com/dp/B002SZEOLG/ref=sr_ph_1?m=ATVPDKIKX0DER&ie=UTF8&qid=1440124668&sr=sr-1&keywords=tplink+high+gain on my Pi and it works really well.

WPA/WPA2 decryption *should* work out of the box (once you configure Wireshark, as tshark uses Wireshark's configuration profile), but it's finnicky. 