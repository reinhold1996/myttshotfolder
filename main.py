"""
Diese Datei sollte eine Konsole ergeben, die unter Linux in einem Screen ausgeführt werden kann. Sie ist als Dienst nicht in verwendung.
"""


import threading
from programm.loop.isrunning import isrunning
from programm.loop.loop import mainloop, preloop
from programm.filemanagement.deleter import movetoold, deleteoutofold





def foreground():
    isrunning.start()
    print("Der Hotfolder wurde aktiviert!")
    print("Folgende Befehle sind bekannt:")
    print("start - startet den Hotfolder")
    print("stop - stoppt den Hotfolder")
    print("status - gibt den Status aus")
    print("generate - erstellt eine servicedatei sowie eine .sh Startdatei!")
    print("exit - beendet das Programm!")
    while True:
        eingabe = input(str(""))
        print(mainloopvar)
        if eingabe.upper() == "HELP":
            print("Folgende Befehle sind bekannt:")
            print("start - startet den Hotfolder")
            print("stop - stoppt den Hotfolder")
            print("status - gibt den Status aus")
            print("generate - erstellt eine servicedatei sowie eine .sh Startdatei!")
            print("exit - beendet das Programm!")

        elif eingabe.upper() == "START":
            status = isrunning.getStatus()
            if status == True:
                print("Hotfolder läuft bereits!")
            elif status == False:
                print("Hotfolder wird gestartet.")
                isrunning.start()
            else:
                print("Fehler bei befehl 'start'")

        elif eingabe.upper() == "STOP":
            status = isrunning.getStatus()
            if status == False:
                print("Hotfolder läuft noch nicht!")
            elif status == True:
                print("Hotfolder beendet!")
                isrunning.stop()
            else:
                print("Fehler bei befehl 'stop'")

        elif eingabe.upper() == "STATUS":
            status = isrunning.getStatus()
            if status == True:
                print("Hotfolder läuft!")
            else:
                print("Hotfolder ist aus!")

        elif eingabe.upper() == "EXIT":
            print("Beenden (0)")
            exit(0)

        elif eingabe.upper() == "GENERATE":
            import programm.first_run.service
            import programm.first_run.startsh
        else:
            print("der Befehlt help gibt alle möglichen Befehle aus.")
            print("Bitte geben Sie help ein.")

preloop()
mainloopvar = threading.Thread(name="mainloop", target=mainloop)
toold = threading.Thread(name="toold", target=movetoold)
deleter = threading.Thread(name="deleter", target=deleteoutofold)
#konsole = threading.Thread(name="foreground", target=foreground)

mainloopvar.setDaemon(True)
toold.setDaemon(True)
deleter.setDaemon(True)

mainloopvar.start()
toold.start()
deleter.start()
#konsole.start()
foreground()