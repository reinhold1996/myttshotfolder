"""
Diese Datei enthölt die Funktionen, die im working/working ordner durchgeführt werden.
"""

from time import sleep

def unheader(fileinput):
    """
    Der unheader entnimmt den Header einer datei und speichert den inhalt in die settings variable.
    """
    file = open(fileinput)
    data = []
    for i in file:
        data.append(i.strip())
    file.close()
    data = data[0]
    data = data.replace("[", "").replace("]","").split(",")
    settings = []
    for i in data:
        i = i.strip()
        anfang = i.find("{")+1
        ende = i.find("}")
        settings.append(i[anfang:ende])
    sleep(0.5)
    return settings

def splitter(splitter, filename="test", textfolder="/home/rodja/PycharmProjects/GTTS_MINIMAL/working/working/2021-04-06 19:51:30 test", fileinput="/home/rodja/PycharmProjects/GTTS_MINIMAL/working/working/2021-04-06 19:51:30 test/test.txt"):
    """
    Der Splitter spaltet eine Eingangsdatei anhand eines seperators (; ist der standard) in einzelne Textdateien, damit man getrennte .mp3 bekommt.
    """
    file = open(fileinput, "r", encoding="UTF-8")
    data = []
    for i in file:
        data.append(i.strip())
    file.close()

    text = ""
    for i in range(1,len(data)):
        text = text + data[i].strip()
    text = text.split(splitter)

    if len(text) == 1:
        for i in range(0, len(text)):
            file = open(textfolder + "/text/" + filename + str(i) + ".txt", "w", encoding="UTF-8")
            file.write(text[i])
            file.close()

    for i in range(0, len(text)-1):
        file = open(textfolder + "/text/" + filename + str(i) + ".txt", "w", encoding="UTF-8")
        file.write(text[i])
        file.close()

    text2 = []
    for i in text:
        if i != "":
            text2.append(i)
    return text2
