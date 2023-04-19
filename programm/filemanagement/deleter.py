"""
Diese Datei ist dafür zuständig alte Outputs, welche älter sind als 30 Tage in den "old" Ordner zu verschieben.
Darüberhinaus verwaltet sie auch den "old" Ordner und löscht die Ordner welche älter sind als ein Jahr.
"""

from programm.logging.logger import log
from programm.filemanagement.mover import move_file
from programm.filemanagement.watcher import watch
from programm.config.path import paths
from datetime import *
from shutil import rmtree
from programm.loop.isrunning import isrunning
from time import sleep


def movetoold():
    """
    Die Funktion movetoold verschiebt Ordner aus dem Input in den old. Dabei ist es Wichtig das die Dateien älter als 30
    Tage sind um verschoben werden zu können.
    """
    Maximales_Alter = 35 # in Tage
    try:
        log.addlog("delter.py movetoold funktion läuft!", "DEBUG")
        while True:
            pfad = isrunning.getPath()
            isrunning_var = open(pfad+"/isrunning.txt").read()
            if isrunning_var == "True":
                actual_time = str(datetime.now())[0:10].split("-")
                actual_time = int(str(int(actual_time[0]) * 365 + int(actual_time[1]) * 31 + int(actual_time[2])))

                listworking = watch(paths.get_working_paths()[4])
                for i in listworking:
                    j = i[0:10].split("-")
                    j = int(j[0]) * 365 + int(j[1]) * 31 + int(j[2])
                    if actual_time - Maximales_Alter > j:
                        move_file(paths.get_working_paths()[4] + "/" + i, paths.get_working_paths()[5] + "/" + i)
                sleep(10)
            else:
                sleep(10)
    except:
        log.addlog("movetoold() aus delter.py ist gecrasht!", "ERROR")


def deleteoutofold():
    """
    Ich lösche alte Daten aus dem old Ordner. Dabei sind die Dateien mindestens ein Jahr alt.
    """
        Maximales_Alter = 370 # in Tage
    try:
        log.addlog("delter.py deleteoutofold funktion läuft!", "DEBUG")
        while True:
            pfad = isrunning.getPath()
            isrunning_var = open(pfad + "/isrunning.txt").read()
            if isrunning_var == "True":
                actual_time = str(datetime.now())[0:10].split("-")
                actual_time = int(str(int(actual_time[0]) * 365 + int(actual_time[1]) * 31 + int(actual_time[2])))

                listold = watch(paths.get_working_paths()[5])

                for i in listold:
                    j = i[0:10].split("-")
                    j = int(j[0]) * 365 + int(j[1]) * 31 + int(j[2])
                    if actual_time - Maximales_Alter > j:
                        rmtree(paths.get_working_paths()[5] + "/" + i)
                sleep(10)
            else:
                sleep(10)
    except:
        log.addlog("deleteoutofold() aus delter.py ist gecrasht!", "ERROR")
