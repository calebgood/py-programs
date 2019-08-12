from pynput import keyboard,mouse

def full_box():
   COMBINATION = {keyboard.Key.ctrl_l}
   # The currently active modifiers
   current = set()
   global value
   global coords
   coords = list()
   value=False
   def on_press(key):
       global value
       if key in COMBINATION:
           current.add(key)
           if all(k in current for k in COMBINATION):
               value=True
       if key == keyboard.Key.esc:
           listener.stop()

   def on_release(key):
       global value
       try:
           current.remove(key)
           coords=[]
           value=False
       except KeyError:
           pass

   def on_click(x, y, button, pressed):
       global value
       global coords
       if pressed and button==mouse.Button.left:
           if value:
               coords.append(x)
               coords.append(y)
               print("pos:",x,y)
               if len(coords)==4:
                  print("done")
                  listener.stop()
                  mou.stop()
   with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    with mouse.Listener(on_click=on_click) as mou:
        print('begin')
        listener.join()
        mou.join()
   return coords
        
def wid_ht_find():               #finds width and height using boxfind
   x=full_box()
   print("Width:",abs(x[0]-x[2]))
   print("Height:",abs(x[1]-x[3]))
   return x

if __name__=="__main__":
  print("co-ordinates:",wid_ht_find())
