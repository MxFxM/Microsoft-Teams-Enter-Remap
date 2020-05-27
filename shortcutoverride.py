from win32gui import GetWindowText, GetForegroundWindow
import time
import keyboard

alreadyMapped = False

while True:
    time.sleep(0.1)
    if "Microsoft Teams" in GetWindowText(GetForegroundWindow()):
        if not alreadyMapped:
            alreadyMapped = True
            #keyboard.block_key('enter')
            keyboard.remap_key('enter', 'shift+enter')
            #keyboard.remap_hotkey('ctrl+enter', 'enter')
            #keyboard.remap_key('#', 'shift+enter')
    else:
        alreadyMapped = False
        keyboard.unhook_all()