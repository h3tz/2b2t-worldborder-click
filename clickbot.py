#!/usr/bin/env python
""" Short description of this Python module.
This file is part of the 2B2T worldborder click. While using
Minecraft Impact serving Bariton, it is just handling default Bariton
commands to semiautomatically reach world border properly.

Longer description of this module.
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Andreas Hetz"
__contact__ = "hetzandreas@gmail.com"
__copyright__ = "Copyright 2020, Hetz Engineering"
__credits__ = ["cabaletta/baritone"]
__date__ = "2020/12/03"
__deprecated__ = False
__email__ =  "hetzandreas@gmail.com"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.1.0"

import logging
import sys
import time
from datetime import datetime
from threading import Thread, Event
from pynput.keyboard import Key, Controller

worldBorderRunV = "0.1"
keyboardTypeSpeedDefault = 0.15 #sec
scriptRuneTimeDefault_s = 21600 #21600sec = 6h
baritonCommandWaitDefault = 0.5 #sec
baritonWalkDefault = 600 #sec
baritonMineDefault = 5 #sec
baritonGoTo = "3000000 120 0"
baritonWaitBetweenCommands = 5 #sec
baritonMineOre = "obsidian netherrack"
startupWaitDefault = 10 #sec

preText = "WORLDBORDER BOT "
motd = [f'{preText} Logic is the beginning of wisdom not the end',
        f'{preText} Highly illogical',
        f'{preText} Live long and prosper',
        f'{preText} Things are only impossible until they re not',
        f'{preText} Insufficient facts always invite danger',
        f'{preText} KHAAANNN',
        f'{preText} It is the lot of man to strive no matter how content he is',
        f'{preText} Without freedom of choice there is no creativity',
        f'{preText} To boldly go where no man has gone before']

keyboard = Controller()
stop = Event()
root = logging.getLogger()
root.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
root.addHandler(handler)
root.info(f'--------------------------')
root.info(f'Worldborder click V{worldBorderRunV}')
root.info(f'--------------------------')
root.info(f'Start: {datetime.now()}')
root.info(f'--------[Setup]------------')
root.info(f'GoTo: {baritonGoTo}')
root.info(f'Walk for: {baritonWalkDefault} seconds then mine {baritonMineOre} for {baritonMineDefault} seconds.')
root.info(f'Enable AUTOEAT manually')
root.info(f'--------[Run]------------')
root.info(f'Switch to Minecraft window manually. Script will start in:')
for countdown in range(1, startupWaitDefault+1):
    time.sleep(1)
    root.info(startupWaitDefault-countdown)

def pressKey(key):
    """
    Press and release a keyboard key
    :param key:
    """
    keyboard.press(key)
    keyboard.release(key)

def _typeSimulation(stringToPrint):
    """
    Type on keybord a given Text. Special characters and ALT, SHIFT, STRG combinations are not supported
    :param stringToPrint:
    """
    for char in stringToPrint:
        time.sleep(keyboardTypeSpeedDefault)
        keyboard.press(char)
    time.sleep(1)
    pressKey(Key.enter)

def writeChatText(chatText):
    """
    Type on keybord a given Text. Special characters and ALT, SHIFT, STRG combinations are not supported
    :param chatText:
    """
    pressKey('t')
    pressKey('t')
    time.sleep(baritonCommandWaitDefault)
    _typeSimulation(chatText)

def setBariton(command, executeTime):
    """
    Set Bariton command. This includes pressing the commandline using t command.
    :param command:
    :param executeTime:
    """
    logging.info(f'Info: {command}')
    pressKey('t')
    pressKey('t')
    time.sleep(baritonCommandWaitDefault)
    _typeSimulation(f'#{command}')
    time.sleep(executeTime)

def goOnTrack():
    """
    Main script to start walking till world border.
    Includes walking, minding, waiting (eating). Repeat
    """
    direction = False
    time.sleep(startupWaitDefault)
    while not stop.is_set():
        setBariton(f'stop',baritonWaitBetweenCommands)
        setBariton(f'goto {baritonGoTo}', baritonWalkDefault)
        setBariton(f'stop',baritonWaitBetweenCommands)
        setBariton(f'mine {baritonMineOre}', baritonMineDefault)
        time.sleep(3)
        #writeChatText(random.choice(motd))


thread = Thread(target=goOnTrack)
thread.start()
thread.join(timeout=scriptRuneTimeDefault_s)
stop.set()

 #time.sleep(randint(5,10))
        ##keyboard.press(Key.esc)
        #time.sleep(10)
        #if direction == False:
        #    pyautogui.moveRel(0, 15, duration=2)
        #   direction = True
        #else:
        #   pyautogui.moveRel(0, -15, duration=2)
#   direction = False