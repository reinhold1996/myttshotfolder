"""
Diese Datei regelt den input Ordner und erstellt die Ordnerstruktur für die Zukunft. Dabei wird der Ordner mit einem
Zeitstempel versetzt und im Ordner befindet sich dann die Ursprungs Datei sowie die Ordner speech, in der die .mp3
Dateien abgelegt werden, und text, in dem die aufgespaltenen Textdateien gespeichert werden.
"""


from datetime import *
from os import mkdir
from initial import paths
from programm.logging.logger import log
from programm.filemanagement.mover import *
from programm.filemanagement.watcher import watch
from time import sleep

working_paths = paths.get_working_paths()


def watchforfile():
    global working_paths
    return len(watch(working_paths[2]))


def fileinput():
    global working_paths
    if len(watch(working_paths[2])) == 0:
        return None

    log.addlog("Datei im Input Ordner!", "DEBUG")
    input_dir = watch(working_paths[2])[0].split(".")

    actual_time = str(datetime.now())[0:10].split("-")
    actual_time_int = int(str(int(actual_time[0]) * 365 + int(actual_time[1]) * 31 + int(actual_time[2])))
    actual_time = str(datetime.now())[0:19].replace(":", "-")
    new_folder = actual_time + " " + input_dir[0]
    mkdir(working_paths[3]+ "/" + new_folder)
    mkdir(working_paths[3] + "/" + new_folder + "/speech")
    mkdir(working_paths[3] + "/" + new_folder + "/text")
    move_file(working_paths[2] + "/" + input_dir[0] + "." + input_dir[1], working_paths[3]+ "/" + new_folder + "/" + input_dir[0] + "." + input_dir[1])
    sleep(0.5)


    return working_paths[3]+ "/" + new_folder + "/" + input_dir[0] + "." + input_dir[1], working_paths[3]+ "/" + new_folder, input_dir[0], new_folder