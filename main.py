from pynput import keyboard

def on_press(key):
    if hasattr(key, 'char') and key.char == 'q':
        keyboard.Controller().press('w')

def on_release(key):
    #print('{0} released'.format(
    #    key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    try:
        if key.char == 'w':
            print('w released')
    except AttributeError:
        return

# ...or, in a non-blocking fashion:
#listener = keyboard.Listener(
#    on_press=on_press,
#    on_release=on_release)
#listener.start()

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

    