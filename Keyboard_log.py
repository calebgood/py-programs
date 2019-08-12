from pynput import keyboard

# The key combination to check
COMBINATION = {keyboard.Key.shift, keyboard.Key.ctrl_l,keyboard.KeyCode.from_char('x')}
print("COMBOX:",COMBINATION)
# The currently active modifiers
current = set()

def on_press(key):
    #print(key)
    if key in COMBINATION:
        current.add(key)
        #print('current:',current)
        if all(k in current for k in COMBINATION):
            print('All modifiers active!')
    if key == keyboard.Key.esc:
        listener.stop()


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print('begin')
    listener.join()
