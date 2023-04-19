"""
Diese Datei kümmert sich darum Ordner und Dateien von ein Verzeichniss ins andere zu schieben.
"""
from os import replace


def move_file(eingang, ausgang):
    replace(eingang, ausgang)


def move_folder(eingang, ausgang):
    replace(eingang, ausgang)
