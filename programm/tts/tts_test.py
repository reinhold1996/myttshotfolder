"""
Diese Datei führt für jede aufgespaltene textdatei eine Cloud anfrage und speichert dann die gesprochene Sprache als .mp3 in den speech ordner.
"""


from google.cloud import texttospeech
from programm.config.path import paths
from os import environ
from time import sleep

try:
    main_path = paths.get_main_path()
    open(main_path + "/programm/tts/gtts.json", "r", encoding="utf-8").close()
    environ["GOOGLE_APPLICATION_CREDENTIALS"] = main_path + "/programm/tts/gtts.json"
    print("Dienstschüssel erfolgreich geladen!", "DEBUG")
except FileNotFoundError:
    print("Dienstschlüssel nicht gefunden! Programm beendet!", "ERROR")
    exit("Dienstschlüssel nicht gefunden!")

sleep(1)

def gtospeech(TEXT, OUTPUT, lang=True, langname=True):

    client = texttospeech.TextToSpeechClient()

    obj = open(TEXT, "r", encoding="UTF-8")
    x = ""
    print("programm/tts/tts.py" + str(TEXT) + "wurde geladen!", "HIG")
    sleep(1)

    for i in obj:
        i = i.strip()
        x = x + i
    obj.close()

    print("programm/tts/tts.py" + str(TEXT) + "in Variable gespeichert!", "LOW")
    sleep(1)

    synthesis_input = texttospeech.SynthesisInput(text=x)

    print("programm/tts/tts.py sammelt informationen aus Configuration!", "LOW")
    sleep(1)

    voice = texttospeech.VoiceSelectionParams(
        language_code=lang, name=langname
    )

    print("programm/tts/tts.py VoiceSelectionParams gewählt!", "LOW")
    sleep(1)

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    print("programm/tts/tts.py AudioEncoding gewählt!", "LOW")
    sleep(1)

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    print("Warte auf Antwort!", "LOW")
    sleep(1)

    with open(OUTPUT, "wb") as out:
        out.write(response.audio_content)
        print("programm/tts/tts.py Audio gespeichert als:" + str(TEXT.split(".")[1]) + ".mp3", "HIGH")
        sleep(1)