"""
Diese Klasse steuert das Logging! Sie speichert die Logs in /working/logs logs werden nach Systemzeit gespeichert.
Logs werden mindestens 5 Tage lang gespeichert und dienen Ausschließlich zum Debuggen.
"""


from datetime import *
from os import path
from os import mkdir
from os import listdir
from os import remove



class Logger:
    loggerofhint = 0

    def __init__(self):
        self.__logs = []
        actual_time = str(datetime.now())[0:10].split("-")
        self.__actual_time = str(int(actual_time[0]) * 365 + int(actual_time[1]) * 31 + int(actual_time[2]))
        self.__path = open(str(path.dirname(path.abspath(__file__)).replace("/programm/logging", "")) +
                           "/programm/config/path/log_path.txt", "r").read()
        self.__path = self.__path.strip()
        self.__log_status = open(str(path.dirname(path.abspath(__file__)).replace("/programm/logging", "")) +
                                 "/programm/config/path/log_status.txt", "r").read().upper()
        try:
            mkdir(self.__path)
        except FileExistsError:
            pass
        dirlist = listdir(self.__path)
        for i in dirlist:
            i = i.split(".")
            if i[0] != self.__actual_time:
                remove(self.__path + "/" + i[0] + "." + i[1])

        # open(self.__path + "/" + self.__actual_time + ".txt", "w", encoding="UTF-8").close()

    def addlog(self, log, level):
        if self.__log_status == "TRUE":
            log = ("[" + str(datetime.now())[11:19] + "] [" + str(level).upper() + "] [" + str(log) + "]")
            self.savelog(log)
        else:
            if Logger.loggerofhint == 0:
                Logger.loggerofhint += 1
                print("LOG IST AUS!")

    def savelog(self, tosavelog):
        save = open(self.__path + "/" + self.__actual_time + ".txt", "a", encoding="UTF-8")
        save.write(tosavelog + "\n")
        save.close()
        # self.log_delter()

    def log_delter(self):
        liste = []
        to_delete = []
        for i in sorted(listdir(self.__path)):
            liste.append(i.split(".")[0])
            if int(i.split(".")[0]) + 7 < int(self.__actual_time):
                to_delete.append(i)
        if len(to_delete) >= 1:
            for i in to_delete:
                remove(str(self.__path)+"/"+i)


log = Logger()
