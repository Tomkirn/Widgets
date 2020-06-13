#!python3

'''
Dieses Widget stellt einen simplen Launcher dar
und zeigt die interne und externe IP
'''

import appex
import ui
import socket
import datetime

def time_to_holiday(y,m,d):
	delta = (datetime.date(y, m, d) - datetime.date.today())
	tage = delta.days
	tagetxt = str(tage)+' Tage'
	if tage > 100:
		symbol = '☹️'
	elif tage > 50:
		symbol = '😕'
	elif tage > 10:
		symbol = '🙂'
	else:
		symbol = '😁'
	return tagetxt, symbol

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

vfont = ('<system>', 14)
efont = ('<system>', 30)
view = ui.View()

#label1 = ui.Label(font=vfont, text='IP: '+get_local_ip())
label1 = ui.Label(font=vfont, text='September Urlaub: '+time_to_holiday(2020,9,28)[0])
#label2 = ui.Label(font=vfont, text='eIP: '+get_global_ip())
label2 = ui.Label(font=vfont, text='Keksbackwoche: '+time_to_holiday(2020,11,23)[0])
label3 = ui.Label(font=vfont, text='Juist: '+time_to_holiday(2021,5,30)[0])
label4 = ui.Label(font=efont, text=time_to_holiday(2021,5,30)[1])

button1 = ui.Button(title=' ⚓️ NavTex ', font=vfont, border_width=0, action=button_action, name='pythonista3://NavTest.py?action=run&root=icloud', corner_radius=9, bg_color='#00ffde')
button2 = ui.Button(title=' 🌦 DWD Wetter ', font=vfont, border_width=0, action=button_action, name='pythonista3://DWDWetter.py?action=run', corner_radius=9, bg_color='#00ffde')

view.add_subview(label1)
view.add_subview(label2)
view.add_subview(label3)
view.add_subview(label4)
view.add_subview(button1)
view.add_subview(button2)

appex.set_widget_view(view)

label1.frame = (150, 10, 220, 35)
label2.frame = (150, 35, 220, 35)
label3.frame = (150, 60, 220, 35)
label4.frame = (view.width-60,60,50,35)

button1.frame = (10, 15, 120, 35)
button2.frame = (10, 60, 120, 35)
