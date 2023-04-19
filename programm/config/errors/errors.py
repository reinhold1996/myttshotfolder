from os import path, remove

class errors2:
    def __init__(self):
        self.__pfad = str(path.dirname(path.abspath(__file__))) + "/errors.txt"
        try:
            remove(self.__pfad)
            open(self.__pfad, "w", encoding="UTF-8").close
        except FileNotFoundError:
            open(self.__pfad, "w", encoding="UTF-8").close

    def get_path(self):
        return self.__pfad

    def del_error(self, errorcode):
        pass

    def write_offline_error(self, errorcode):
        pass

    def write_error(self, errorcode):
        openedfile = open(self.__pfad, "a", encoding="UTF-8")
        openedfile.write(errorcode+"\n")

Save_To_Error = errors2()