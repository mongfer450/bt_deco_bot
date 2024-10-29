import pyautogui
import time
import keyboard

# List of positions with image data instead
images = [
    # สูตร cm
    {"id": 1, "image": "./resource/i1.png"},
    {"id": 2, "image": "./resource/i2.png"},
    {"id": 3, "image": "./resource/i3.png"},
    {"id": 4, "image": "./resource/i4.png"},
    {"id": 5, "image": "./resource/i5.png"},
    {"id": 6, "image": "./resource/i6.png"},
    {"id": 7, "image": "./resource/i7.png"},
    {"id": 8, "image": "./resource/i8.png"},
    {"id": 9, "image": "./resource/i9.png"},
    {"id": 10, "image": "./resource/i10.png"},
    {"id": 11, "image": "./resource/i11.png"},
    {"id": 12, "image": "./resource/i12.png"},
    {"id": 13, "image": "./resource/i13.png"},
    {"id": 14, "image": "./resource/i14.png"},
    {"id": 15, "image": "./resource/i15.png"},
    {"id": 16, "image": "./resource/i16.png"},
    {"id": 17, "image": "./resource/i17.png"},

    # สูตร rare
    # {"id": 1, "image": "./resource/i1.png"},
    # {"id": 2, "image": "./resource/i2.png"},
    # {"id": 3, "image": "./resource/i3.png"},
    # {"id": 4, "image": "./resource/i4.png"},
    # {"id": 5, "image": "./resource/i5.png"},
    # {"id": 6, "image": "./resource/i6.png"},
    # {"id": 7, "image": "./resource/i7.png"},
    # {"id": 8, "image": "./resource/i8.png"},
    # {"id": 9, "image": "./resource/i9.png"},
    # {"id": 10, "image": "./resource/i10.png"},
    # {"id": 11, "image": "./resource/i11.png"},
    # {"id": 12, "image": "./resource/i12.png"},
    # {"id": 13, "image": "./resource/i13.png"},
    # {"id": 14, "image": "./resource/i14.png"},
    # {"id": 15, "image": "./resource/i15.png"},
    # {"id": 16, "image": "./resource/i16.png"},
    # {"id": 17, "image": "./resource/i17.png"},

    {"id": 21, "image": "./resource/btn_reclaim.png"},   # Reclaim 
    {"id": 22, "image": "./resource/btn_place.png"},  # Place
]

# Global flag to control startPlaceDeco execution
stop_place_deco = False

# Helper function to sleep with frequent key-checking
def sleep_with_key_check(duration):
    global stop_place_deco
    check_interval = 0.1  # Interval for checking key press in seconds
    for _ in range(int(duration / check_interval)):
        if keyboard.is_pressed('n'):  # Check if 'n' is pressed to exit startPlaceDeco only
            stop_place_deco = True  # Set flag to stop startPlaceDeco
            print("stop_place_deco flag set to True")
            return True  # Signal to exit sleep early
        time.sleep(check_interval)
    return False  # Continue as normal

# Function to find a picture by ID and click it
def clickItem(target_id, delay):
    time.sleep(0.3)
    if stop_place_deco:
        return True  # Stop if the flag is set

    pictureID = next((item for item in images if item["id"] == target_id), None)  # find pic id

    if pictureID:
        counter = 0
        while counter < 1:
            try:
                locatedPic = pyautogui.locateCenterOnScreen(pictureID["image"], confidence=0.8)  # 1. find pic in screen
                if locatedPic:
                    print(f'Found ID:{target_id}')
                    if sleep_with_key_check(delay):  # 2. Check during delay
                        return True
                    pyautogui.moveTo(locatedPic)
                    pyautogui.click(locatedPic)  # 3. click at pic
                    break  # break loop if the image is found and clicked
                else:
                    print(f"Can't find ID: {target_id} on Screen")
                    time.sleep(0.3)  # Small delay before retrying
            except pyautogui.ImageNotFoundException:
                if sleep_with_key_check(0.1): return
                print(f"Can't find Image ID {target_id}")
                time.sleep(0.3)  # Small delay before retrying
                
    else:
        print(f"Can't find ID:{target_id} in data")
    return False


def placeDeco(start,end,id):
    global stop_place_deco
    for i in range(start,end):
        if stop_place_deco:  # Check flag to stop
            return
        print(f"Placed: {id} \n")
        
        if sleep_with_key_check(0.3):  # Check for 'n' key press to exit before each loop
            return

        pyautogui.press('b')
        print("Open deco window")
        if sleep_with_key_check(0.2): return

        if clickItem(id, 0.1): return
        print(f"Select Item {id}")
        if sleep_with_key_check(0.1): return

        if clickItem(21, 0.1): return
        if sleep_with_key_check(0.5): return
        if clickItem(22, 0.1): return
        print("Reclaim & place")
        if sleep_with_key_check(1): return

        print("Macro Running...")
        pyautogui.click()
        if sleep_with_key_check(1.5): return
        pyautogui.press('b')
        if sleep_with_key_check(0.02): return
        pyautogui.click()
        if sleep_with_key_check(0.8): return
        pyautogui.press('esc')
        if sleep_with_key_check(1): return
        pyautogui.keyDown('w')
        if sleep_with_key_check(0.005): return
        pyautogui.keyUp('w')
        print("------------")


def setA(): #Mythic 2 Legend 8 Epic 4 Rare 10 Uncommon 8 Common 2
    for i in range(1, 18): 
        placeDeco(1, 3, i) 
        
def setB(): #Mythic 2, Legend 8, Epic 4, Rare 4
    placeDeco(1, 3, 1)  #ปัก Mythic 2
    for i in range(2, 9): #ปัก leg 8, epic 4, rare 4 
        placeDeco(1, 3, i)
    print("End")

def setC(): #Mythic 6, Uncm 6 
    placeDeco(1, 4, 1) 
    placeDeco(1, 3, 13) 
    placeDeco(1, 3, 14) 
    placeDeco(1, 3, 15) 

def startPlaceDeco(setsChoose):
    global stop_place_deco
    stop_place_deco = False  #Reset the flag when starting

   
    print("Start Placing...")
    if sleep_with_key_check(1): return

    setsChoose()

def startProgram():
    print('Program Start')
    print('--------------------------')
    while True:
        time.sleep(0.2)
        if keyboard.is_pressed('y'):
            print('select 1,2,3')
            while True:
                time.sleep(0.2)
                if keyboard.is_pressed('1'):
                    print('Placing SetA')
                    print('-')
                    startPlaceDeco(setA)
                elif keyboard.is_pressed('2'):
                    print('Placing SetB')
                    print('-')
                    startPlaceDeco(setB)
                elif keyboard.is_pressed('3'):
                    print('Placing SetC')
                    print('-')
                    startPlaceDeco(setC)

startProgram()
