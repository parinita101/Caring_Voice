import os
import eel #gui

from engine.feature import * # start sound hai jo kaam nhi kar rha
from engine.command import*
eel.init("www")

playAssistantSound()



os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html',mode=None,host='localhost', block=True) 