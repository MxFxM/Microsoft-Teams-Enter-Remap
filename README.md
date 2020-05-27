# Microsoft-Teams-Enter-Remap
It bugged me that I cannot remove or change the send on enter from MS Teams, so I did this...

## How to use
Start the .exe file in the relase folder.

It will run in the background and uuse about 10Mb RAM.
I know that is much but I don't care since 1) I want to run it 2) my PC has more than enough RAM.

## How it works
The code constantly checks the focused window.
If the name of the window includes "Microsoft Teams" (it will also include the name of the chat...),
the script will rebind enter to shift+enter.
That way you can no longer send using enter, but it will place a line break.

## Dependencies
The .exe runs without dependencies.

The code will require:
- Pywin32: https://github.com/mhammond/pywin32
- Keyboard: https://github.com/boppreh/keyboard#api

## Confirmed working
- Windows 10 64bit
