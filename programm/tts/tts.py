"""
Diese Datei führt für jede aufgespaltene textdatei eine Cloud anfrage und speichert dann die gesprochene Sprache als .mp3 in den speech ordner.
"""


from google.cloud import texttospeech
from programm.logging.logger import log
from programm.config.path import paths
from programm.google_login import *
from os import environ

try:
    main_path = paths.get_main_path()
    open(main_path + "/programm/tts/gtts.json", "r", encoding="utf-8").close()
    environ["GOOGLE_APPLICATION_CREDENTIALS"] = main_path + "/programm/tts/gtts.json"
    log.addlog("Dienstschüssel erfolgreich geladen!", "DEBUG")
except FileNotFoundError:
    log.addlog("Dienstschlüssel nicht gefunden! Programm beendet!", "ERROR")
    exit("Dienstschlüssel nicht gefunden!")

def gtospeech(TEXT, OUTPUT, lang=True, langname=True):
    log.addlog("programm/tts/tts.py   gtospeech() wurde ausgeführt!", "LOW")

    client = texttospeech.TextToSpeechClient()

    obj = open(TEXT, "r", encoding="UTF-8")
    x = ""
    log.addlog("programm/tts/tts.py" + str(TEXT) + "wurde geladen!", "HIG")

    for i in obj:
        i = i.strip()
        x = x + i
    obj.close()

    log.addlog("programm/tts/tts.py" + str(TEXT) + "in Variable gespeichert!", "LOW")

    synthesis_input = texttospeech.SynthesisInput(text=x)

    log.addlog("programm/tts/tts.py sammelt informationen aus Configuration!", "LOW")

    voice = texttospeech.VoiceSelectionParams(
        language_code=lang, name=langname
    )

    log.addlog("programm/tts/tts.py VoiceSelectionParams gewählt!", "LOW")

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    log.addlog("programm/tts/tts.py AudioEncoding gewählt!", "LOW")

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    log.addlog("Warte auf Antwort!", "LOW")

    with open(OUTPUT, "wb") as out:
        out.write(response.audio_content)
        log.addlog("programm/tts/tts.py Audio gespeichert als:" + str(TEXT.split(".")[1]) + ".mp3", "HIGH")