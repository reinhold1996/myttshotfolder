"""
Diese Datei ist dafür zuständig den Inhalt von Ordnern in dem Angegebenen Pfad anzuzeigen. Dazu wird das modul listdir
aus dem Paket os verwendet.
"""


from os import listdir


def watch(path):
    return listdir(path)
