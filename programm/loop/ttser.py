"""
Diese Datei übergibt die gespaltenen Textdateien in das Google TTS Modul
"""


from programm.tts.tts import gtospeech
from programm.filemanagement.watcher import watch

def texttospeech(lang, langname, inputfolder, output_folder):
    filenames = watch(inputfolder)
    for i in filenames:
        gtospeech(inputfolder + "/" + i, output_folder + "/" + i.split(".")[0] + ".mp3", lang, langname)
