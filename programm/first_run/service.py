"""
[Install]
WantedBy=multi-user.target

[Unit]
Description=Google Cloud tts

[Service]
ExecStart=placeholder
User=REPLACE_USERNAME
Restart=on-failure
RestartSec=30
"""
from programm.config.path import paths
pfad = paths.get_main_path()

service_file = "[Install]", "WantedBy=multi-user.target", "", "[Unit]", "Description=Google Cloud tts", "", \
               "[Service]", "ExecStart=placeholder", "User=USERNAME", "Restart=on-failure", "RestartSec=30"
save = open(pfad + "/servicedatei.service", "w", encoding="UTF-8")
for i in service_file:
    i = i.replace("placeholder", pfad)
    save.write(i+"\n")
save.close()