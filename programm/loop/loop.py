"""
Diese Datei enthölt die Funktion für die Hauptschleife. Vom eingang der Datei in das Input verzeichniss bis hin zur fertigen .mp3 Datei!
"""
from programm.config.path import paths
from programm.logging.logger import log
from programm.filemanagement.mover import move_file
from programm.filemanagement.folder_creator import create_folders
from programm.loop.input import fileinput, watchforfile
from programm.loop.working import unheader
from programm.loop.working import splitter
from programm.loop.ttser import texttospeech
from programm.loop.isrunning import isrunning
from programm.online_checker.onlinechecker import WebCheck
from time import sleep
import platform
from programm.config.errors.errors import Save_To_Error


def preloop():
    """
    Der Preeloop sorgt dafür das der Arbeitsplatz bzw. die Arbeitsordner angelegt sind.
    """
    try:
        log.addlog("Preloop durchlaufen!", "DEBUG")
        create_folders()
    except:
        log.addlog("preloop() aus loop.py ist gecrasht!", "ERROR")

def mainloop():
    """
    Der mainloop ist dafür zuständig das die Dateien aus dem Input Ordner verarbeitet werden.
    """
    try:
        while True:
            os = platform.platform().upper()
            response = None
            if "windows".upper() in os:
                os = ("WINDOWS")
            elif "linux".upper() in os:
                os = ("LINUX")


            pfad = isrunning.getPath()
            isrunning_var = open(pfad+"/isrunning.txt").read()
            if isrunning_var == "True":
                WebCheck.check_connection()
                log.addlog("Mainloop gestartet!", "DEBUG")
                if WebCheck.get_online_status() == "Online":
                    try:
                        somthingininput = watchforfile()
                        if somthingininput >= 1: #prüft ob etwas im Input ordner ist.
                            input = fileinput() #erster arbeitschritt input nach working verschieben und grundliegende Ordnerstruktur erstellen
                            header = unheader(input[0]) #bezieht die Sprachinfos aus dem Header
                            split = splitter(header[2], input[2], input[1], input[0]) #spaltet die Textdatei in einzelne Dateien.
                            texttospeech(header[0], header[1], input[1] + "/text", input[1] + "/speech") #erstellt die .mp3
                            move_file(input[1], paths.get_working_paths()[4] + "/" + input[3]) #verschiebt den Ordner ins Output verzeichniss
                    except:
                        log.addlog("Fehler bei funktion Mainloop programm/loop/loop.py: Ist der Dienstschlüssel gültig?", "ERROR")
                else:
                    log.addlog('Server Offline gemerkt bei programm/loop/loop.py', "ERROR")
            sleep(1)
    except:
        log.addlog("mainloop() aus loop.py ist gecrasht!", "ERROR")


def afterloop():
    """
    der afterloop dient als Platzhalter, hat noch keine Funktion.
    """
    pass
