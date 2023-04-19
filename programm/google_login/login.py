"""
Diese Datei lädt die umgebungsvariable um den Dienstschlüssel für die Google Cloud einzulessen.
"""
from programm.logging.logger import log

from initial import all_paths
from os import environ

paths = all_paths()

try:
    main_path = paths.get_main_path()
    open(main_path + "/programm/tts/gtts.json", "r", encoding="utf-8").close()
    environ["GOOGLE_APPLICATION_CREDENTIALS"] = main_path + "/programm/tts/gtts.json"
    log.addlog("Dienstschüssel erfolgreich geladen!", "DEBUG")
except FileNotFoundError:
    log.addlog("Dienstschlüssel nicht gefunden! Programm beendet!", "ERROR")
