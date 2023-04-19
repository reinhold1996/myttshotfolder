"""
Diese Datei Regelt den Status der Datei und soll als Anzeige dienen, um zu sehen ob das Programm läuft.
"""


from os import path

class loop():
    def __init__(self):
        self.__pfad = str(path.dirname(path.abspath(__file__)))
        self.__isrunning = "False"

    def start(self):
        self.__isrunning = "True"
        write = open(self.__pfad + "/isrunning.txt", "w", encoding="UTF-8")
        write.write("True")

    def stop(self):
        self.__isrunning = "False"
        write = open(self.__pfad + "/isrunning.txt", "w", encoding="UTF-8")
        write.write("False")

    def exit(self):
        self.__isrunning = "exit"
        write = open(self.__pfad + "/isrunning.txt", "w", encoding="UTF-8")
        write.write("exit")

    def getStatus(self):
        file = open(self.__pfad + "/isrunning.txt", "r", encoding="UTF-8").read()
        file = bool(file)
        return file

    def getPath(self):
        return self.__pfad

isrunning = loop()