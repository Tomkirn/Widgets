#!python3

'''
Dieses Widget stellt einen simplen Launcher dar
und zeigt die interne IP und SSID
'''

import appex
import ui
import socket
from objc_util import *

NSBundle.bundleWithPath_('/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework').load()

cNetwork = ['None','WiFi','Cellular']

def currentNetworkType():
	netMon=ObjCClass('SUNetworkMonitor').sharedInstance()
	return netMon.currentNetworkType()
	
def get_ssid():
	CNCopyCurrentNetworkInfo = c.CNCopyCurrentNetworkInfo
	CNCopyCurrentNetworkInfo.restype = c_void_p
	CNCopyCurrentNetworkInfo.argtypes = [c_void_p]
	info = ObjCInstance(CNCopyCurrentNetworkInfo(ns('en0')))
	try:
		ssid = str(info['SSID'])
	except:
		ssid = 'kein WLAN'
	return ssid

def get_local_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		s.connect(('google.com', 80))
		ip = s.getsockname()[0]
		s.close()
	except:
		ip = 'N/A'
	return ip

def get_global_ip():
	#curl http://icanhazip.com
	import requests
	return requests.get('http://icanhazip.com').text

def button_action(sender):
		import webbrowser
		webbrowser.open(sender.name)

view = ui.View()

label1 = ui.Label(font=('Menlo', 18), text='IP: '+get_local_ip())
'''if currentNetworkType() == 1:
	label2 = ui.Label(font=('Menlo', 18), text='SSID: '+get_ssid())
else:
	label2 = ui.Label(font=('Menlo', 18), text='No WiFi')'''
label3 = ui.Label(font=('Menlo', 18), text='eIP: '+get_global_ip())

button1 = ui.Button(title=' ⚓️ NavTex ', border_width=0, action=button_action, name='pythonista3://NavTest.py?action=run&root=icloud', corner_radius=9, bg_color='#00ffde')
button2 = ui.Button(title=' 💻 Pythonista ', border_width=0, action=button_action, name='pythonista3://', corner_radius=9, bg_color='#b1ff00')
button3 = ui.Button(title=' 🌦 DWD Wetter ', border_width=0, action=button_action, name='pythonista3://DWDWetter.py?action=run&root=icloud', corner_radius=9, bg_color='#00ffde')
button4 = ui.Button(title=' 🤡 ', border_width=0, action=button_action, name='pythonista3://', corner_radius=9, bg_color='#b1ff00')

view.add_subview(label1)
#view.add_subview(label2)
view.add_subview(label3)
view.add_subview(button1)
view.add_subview(button2)
view.add_subview(button3)
view.add_subview(button4)
#view.height = 200

appex.set_widget_view(view)

label1.frame = (150, 10, 220, 35)
#label2.frame = (150, 70, 220, 35)
label3.frame = (150, 40, 220, 35)

button1.frame = (10, 15, 120, 35)
button2.frame = (10, 60, 120, 35)
button3.frame = (view.width-130, 15, 120, 35)
button4.frame = (view.width-130, 60, 120, 35)

