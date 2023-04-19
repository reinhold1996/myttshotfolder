"""
Diese Datei Importiert die Arbeitspfade (input/log/output/old usw. aus der initial.py im Hauptverzeichniss.
"""


from initial import paths


main_paths = paths.get_main_path()
working_paths = paths.get_working_paths()
