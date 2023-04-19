"""
Diese Datei erstellt einige Variablen die im späteren Verlauf benötigt werden!
Darunter wird der Pfad des Programms ermittelt sowie schonmal das Arbeitsverzeichniss.
"""
from os import path
from programm.logging.logger import log


class all_paths():
    def __init__(self):
        self.__working_path = open(str(path.dirname(path.abspath(__file__))) + "/programm/config/path/working_path.txt").read()
        print(self.__working_path)
        self.__working_path = self.__working_path.strip()


        self.__main_path = str(path.dirname(path.abspath(__file__)))

        self.__working_paths = self.__working_path, self.__working_path + "/logs", self.__working_path + "/input", self.__working_path + "/working", self.__working_path + "/output", self.__working_path + "/old"
        log.addlog("Arbeitspfade geladen!", "debug")
        file = open(self.__main_path + "/programm/config/path/log_path.txt", "w", encoding="UTF-8")
        print("Log path geschrieben:", self.__working_paths[1])
        file.write(self.__working_paths[1])

    def get_main_path(self):
        return self.__main_path

    def get_working_paths(self):
        return self.__working_paths

    def write_log_path(self):
        pass

paths = all_paths()