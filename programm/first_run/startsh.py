"""
#!/bin/bash
placeholder
python3 start.py
"""
from programm.config.path import paths
pfad = paths.get_main_path()

startsh_file = "#!/bin/bash", "cd placeholder", "python3 start.py"
save = open(pfad + "/start.sh", "w", encoding="UTF-8")
for i in startsh_file:
    i = i.replace("placeholder", pfad)
    save.write(i+"\n")
save.close()