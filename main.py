import pyautogui
from time import sleep
import os

def main():
    
    initializePyAutoGUI()
    countdownTimer()
        
# =============================================================================
#     checkGameOver()
# =============================================================================
#     playGame()
# =============================================================================
#     openDoor()
# =============================================================================
    
# =============================================================================
    startNewGame()
# =============================================================================
# =============================================================================
#     reportMousePosition()
# =================================================

    print("Done")


def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = True


def countdownTimer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 3):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")

def reportMousePosition(seconds=10):
    for i in range(0, seconds):
        print(pyautogui.position())
        sleep(1)
        
def startNewGame():
    # Click on new game
    sleep(3)
    pyautogui.click(400, 885, duration=0.1)
    pyautogui.click(400, 885, duration=0.2)

    # Click on "Too Easy"
    sleep(3)
    pyautogui.click(130, 405)

    # Click Sara
    sleep(2)
    pyautogui.click(x=645, y=820)

    sleep(2)
    pyautogui.click(1770, 1010, duration=0.3)

    sleep(2)
    # Skip cutscene (same button)
    pyautogui.click(1770, 1010, duration=0.3)

    sleep(10)
    playGame()

    
def playGame():    
    # Open first door
    count=0
        
    while True:
        ik = openDoor()
        if ik==1:
            count=count+1
            if count==3:
                resetGame()
                return
        else:
            count=0
        sleep(6)
        checkGameOver()
        checkMainMenu()
        pyautogui.press('1')
        sleep(0.2)
        pyautogui.press('1')
        # heal if possible
        pyautogui.click(1708, 68, duration=0.1)
        sleep(0.5)

    return None
    
def openDoor():    
    images_to_check = [
            'door_1080p_001.png',
            'door_1080p_002.png',
            'door_1080p_003.png',
            'door_1080p_004.png',
            'door_1080p_005.png',
            'door_1080p_006.png',
            'door_1080p_007.png',
        ]
    
    # loop over images until one is found, then return the index of the found
    # image
    for index, image_filename in enumerate(images_to_check):
        script_dir = os.path.dirname(__file__)
        Door_path = os.path.join(
            script_dir, 
            'images',
            image_filename)
        try:
            image_pos = pyautogui.locateOnScreen(Door_path, confidence=0.9)
        except Exception as e:
            print(f"Error locating door {index+1}: {e}")
            continue
        else:
            if image_pos:
                print("Door {} found".format(index+1))
                pyautogui.click(x=image_pos[0]+50, y=image_pos[1]+50, button='right')  # right-click the mouse
                sleep(0.2)
                pyautogui.click(x=image_pos[0]+50, y=image_pos[1]+50, button='right')  # right-click the mouse
                return None
                
    return 1
    
def checkGameOver():
    script_dir = os.path.dirname(__file__)
    Door_path = os.path.join(
        script_dir,
        'images', 
        'game_over.png'
    )
    try:
        image_pos = pyautogui.locateOnScreen(Door_path, confidence=0.8)
    except: print("Game not over")
    else:
        if image_pos:
            print("Game over")
            sleep(2)
            pyautogui.click(x=1550, y=1026) 
            sleep(2)
            startNewGame()
            return None
        
def checkMainMenu():
    script_dir = os.path.dirname(__file__)
    Door_path = os.path.join(
        script_dir, 
        'images',
        'main_menu.png'
    )
    try:
        image_pos = pyautogui.locateOnScreen(Door_path, confidence=0.8)
    except: print("Not at main menu")
    else:
        if image_pos:
            print("Reached main menu")
            sleep(0.5)
            sleep(2)
            startNewGame()
            return None  

def resetGame():
    print("Resetting game")
    pyautogui.press('esc')
    sleep(2)
    # Abandon
    pyautogui.click(x=940, y=690) 
    sleep(2)
    # Confirm
    pyautogui.click(x=1100, y=633)
    sleep(2)
    startNewGame()

if __name__ == "__main__":
    main()