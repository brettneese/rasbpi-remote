import os

# def start():
# 	os.system('irsend SEND_ONCE pioneer KEY_POWER')
# 	os.system('irsend SEND_ONCE pioneer KEY_VCR')
# 	return True


# def stop():
# 	os.system('irsend SEND_ONCE pioneer KEY_TV')
# 	os.system('irsend SEND_ONCE pioneer KEY_POWER')
# 	return True


def airplay_toggle():

	os.system('irsend SEND_ONCE pioneer KEY_TV')
	os.system('irsend SEND_ONCE pioneer KEY_POWER')
	os.system('irsend SEND_ONCE pioneer KEY_VCR')
	return True


def tv_toggle():
	os.system('irsend SEND_ONCE pioneer KEY_TV')
	os.system('irsend SEND_ONCE pioneer KEY_POWER')
	os.system('irsend SEND_ONCE pioneer KEY_TV')

	return True


def receiver_volumeup(times=1):
	for _ in range(int(times)):
		os.system('irsend SEND_ONCE pioneer KEY_VOLUMEUP')

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
