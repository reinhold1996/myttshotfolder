from os import remove
from time import sleep
from programm.config.path import paths
texts = "\n\n\nIch Teste den Vorhandenen Dienstschlüssel!","\n", "0 - Beendet das Programm." ,"1 - Lädt den Dienstschlüssel und führt einen Test aus", "2 - Bereinige Testdateien!"
try:
    open(paths.get_main_path()+"/test.txt", "r")
    remove(paths.get_main_path()+"/test.txt")
    print("Testdatei gefunden! -> Lösche")
except:
    print("Keine Testdatei gefunden!")
while True:
    for i in texts:
        print(i)
    try:
        eingabe = int(input("Bitte wählen:"))
        if eingabe == 0:
            exit(0)
        elif eingabe == 1:
            print("TESTE!")
            print(paths.get_main_path())

            testfile = open(paths.get_main_path()+"/test.txt", "w")
            testfile.write("Ich bin eine Testdatei. Ich bin nur zum Testen da!")
            testfile.close()
            print("Testdatei erstell!")
            sleep(1)

            import programm.tts.tts_test as tts
            tts.gtospeech(paths.get_main_path()+"/test.txt" , paths.get_main_path()+"/test.mp3", "de-DE", "de-DE-Wavenet-F")
            remove(paths.get_main_path() + "/test.txt")
            print("test.txt wurde gelöscht!")
            sleep(3)

        elif eingabe == 2:
            try:
                open(paths.get_main_path() + "/test.txt", "r")
                remove(paths.get_main_path() + "/test.txt")
                print("Testdatei 'test.txt' gefunden! -> Lösche")
            except:
                print("Keine 'test.txt' Testdatei gefunden!")
            sleep(0.25)
            try:
                open(paths.get_main_path() + "/test.mp3", "r")
                remove(paths.get_main_path() + "/test.mp3")
                print("Testdatei 'test.mp3' gefunden! -> Lösche")
            except:
                print("Keine 'test.mp3' Testdatei gefunden!")
            sleep(2)

        else:
            print("Eingabe muss 0 oder 1 sein!")
            sleep(2)
    except ValueError:
        print("Eingabe muss eine Zahl sein 0 oder 1!")
        sleep(2)