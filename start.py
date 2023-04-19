"""
Diese Datei dient als service für systemctl.
"""


import threading
from programm.loop.isrunning import isrunning
from programm.loop.loop import mainloop, preloop
from programm.filemanagement.deleter import movetoold, deleteoutofold
from time import sleep

preloop()
isrunning.start()
mainloopvar = threading.Thread(name="mainloop", target=mainloop)
toold = threading.Thread(name="toold", target=movetoold)
deleter = threading.Thread(name="deleter", target=deleteoutofold)

mainloopvar.setDaemon(True)
toold.setDaemon(True)
deleter.setDaemon(True)

mainloopvar.start()
toold.start()
deleter.start()
while True:
    sleep(5)
    isrunning.getStatus()
    if isrunning.getStatus() == "exit":
        exit(0)