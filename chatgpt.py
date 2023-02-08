import keyboard

def handle_hotkey():
    # code to run when hotkey is triggered
    print("Control + mouse wheel up hotkey triggered!")

# bind hotkey to function
keyboard.add_hotkey('ctrl+mousewheel up', handle_hotkey)

# wait for hotkeys to be triggered
keyboard.wait()
