import urllib.request
from os import path, remove
from time import sleep
from programm.config.path import paths

class check_for_internet:
    def __init__(self):
        self.__online = None
        self.__offlinepath = paths.get_working_paths()[2] + "/#1 ONLINECHECK DEAKTIVIERT!"
        if self.__online == None:
            self.check_connection()

    def check_connection(self):
        urls = "https://www.google.de/", "https://www.google.com/"
        onlinelist = []
        for i in urls:
            sleep(0.1)
            try:
                urllib.request.urlopen(i)  # Python 3.x
                onlinelist.append("Online")
            except:
                onlinelist.append("Offline")
        self.__online = onlinelist
        onlinelist = []

    def get_online_list(self):
        self.check_connection()
        return self.__online

    def get_online_status(self):
        self.check_connection()
        if "Offline" in self.__online:
            # open(self.__offlinepath, "w")  // ONLINECHECK DEAKTIVIERT!
            return "Online"
        elif self.__online[0] == "Online" and self.__online[1] == "Online":
            try:
                remove(self.__offlinepath)
            except FileNotFoundError:
                pass
            return "Online"

WebCheck = check_for_internet()