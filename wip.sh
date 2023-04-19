#!/bin/bash
screen -dm bash -c 'cd /home/common/gtts; source /home/common/gtts/virtualenviroment/bin/activate; python3 /home/common/gtts/main.py'
sleep 10s
screen -S bash -p 0 -X "exit"