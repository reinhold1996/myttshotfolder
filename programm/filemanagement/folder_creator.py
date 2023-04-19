"""
Diese Datei erstellt die Arbeitsordner für die weitere Verarbeitung sie wird nach dem Start ein mal ausgeführt.
"""


from programm.logging.logger import log
from programm.config.path import working_paths
import os


def create_folders():
    """
    create_folders erstellt die Ordner im working verzeichniss.
    """
    log.addlog("folder_creator.py create_folders ausgeführt!", "DEBUG")
    for i in working_paths:
        try:
            os.mkdir(i)
            log.addlog("Ordner " + i + " Erstellt!", "DEBUG")
        except FileExistsError:
            log.addlog("Ordner " + i + " Schon vorhanden!", "DEBUG")
