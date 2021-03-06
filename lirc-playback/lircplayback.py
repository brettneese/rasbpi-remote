import os

def airplay_toggle():
	os.system('irsend SEND_ONCE pioneer KEY_TV')
	os.system('irsend SEND_ONCE pioneer KEY_POWER')
	os.system('irsend SEND_ONCE pioneer KEY_VCR')

	return True


def tuner_toggle(volume=None):
	os.system('irsend SEND_ONCE pioneer KEY_TV')
	os.system('irsend SEND_ONCE pioneer KEY_POWER')
	os.system('irsend SEND_ONCE pioneer KEY_VCR')
    if volume is not None:
		receiver_setvolume(int(volume))
	os.system('irsend SEND_ONCE pioneer KEY_TUNER')

	return True


def tv_toggle():
	os.system('irsend SEND_ONCE pioneer KEY_TV')
	os.system('irsend SEND_ONCE pioneer KEY_POWER')
	os.system('irsend SEND_ONCE pioneer KEY_TV')

	return True

def airplay_switch():
	os.system('irsend SEND_ONCE pioneer KEY_VCR')

	return True


def tuner_switch(volume=None):
	if volume is not None:
		receiver_setvolume(int(volume))
	os.system('irsend SEND_ONCE pioneer KEY_TUNER')

	return True


def tv_switch():
	os.system('irsend SEND_ONCE pioneer KEY_TV')

	return True


def receiver_volumeup(times=1):
	for _ in range(int(times)):
		os.system('irsend SEND_ONCE pioneer KEY_VOLUMEUP')

	return True


def receiver_togglemute():
	os.system('irsend SEND_ONCE pioneer KEY_MUTE')

	return True


def receiver_volumedown(times=1):
	for _ in range(int(times)):
		os.system('irsend SEND_ONCE pioneer KEY_VOLUMEDOWN')

	return True


def receiver_fakemute():
	for _ in range(124):
		os.system('irsend SEND_ONCE pioneer KEY_VOLUMEDOWN')

	return True


def receiver_setvolume(value):
	receiver_fakemute()
	for _ in range(int(value)):
		os.system('irsend SEND_ONCE pioneer KEY_VOLUMEUP')

	return True
