# DoTE-I-Could-Quit-If-I-Wanted-To

Python code for opening doors automatically - for the achievement "I Could Quit if I Wanted To" for Dungeon of the Endless

# Setup

- Python version <= 3.11 is required
- pip install pyautogui
- pip install opencv-python

# Introduction

This Python script opens doors in the game "Dungeon of the Endless" automatically in order to get the achievement "I Could Quit if I Wanted To" where you need to open 10,000 doors. In order to run the script, there are two packages you need to install: pyautogui and opencv-python. To do so you can simply create and environment and run "pip install pyautogui" and "pip install opencv-python". pyautogui is a package that produces keyboard and mouse inputs, and is able to capture screenshots and infer object positions based on a reference image. opencv-python just provides the "confidence" argument so that pyautogui has some leeway to fail for the inference. If you are absolutely new to Python you may try googling for Anaconda and install that, then google on how to create an environment and activating it.

The motivation for this script is simple: I've gotten every other achievement in the other game in 60 hours and end up with only 4800 doors opened. The fastest way to open doors is to blaze through level 1 as quickly as possible without fighting, then restart the game once you've opened all the doors or your characters died. Even then this process is mind numbing so I've decided to automate it so that I can stay AFK because I was tired of the game. I have borrowed heavily from someone who has written some pyautogui scripts for botting in his own games too.

Please read the # WARNING paragraph below as it is likely that you will have to make some changes to the script unless you have the exact same computer and monitor as me.

# How does it work?

You start the main menu of the game, where you can see "new game". You have to make sure that "continue" is greyed out and there is no outstanding game to continue on. You may run main.py using either DOS or through your preferred IDE, after which you have to alt+tab back to the game so that you're at the main menu. The script starts a new game ASAP with two random characters. The goal here is to run through as much of level 1 as possible.

Using only the first character, the pyautogui package will attempt to look for a door to open by using the door images in the "image" folder. Upon finding a door, pyautogui will automatically click on the door and your character moves forward. The script will repeat this so long as it can find doors after centering the screen on top of the first character, with some occasional heals. The script WILL NOT exhaustively proceed to every door in the first level. It is likely that you will run into a dead end, and the script will attempt to find a door 3 more times before quitting the game and restarting the process. There is also a chance that both characters will die and you'll proceed to the gameover screen, after which the script will navigate out of that screen and restart the process still. On my computer it is able to clear roughly 250 doors an hour, which I would say is pretty good considering I am AFK. However it is likely that you can't run the script immediately without facing issues, so PLEASE READ ON.

# Issues

1. Key issue here is the resolution of the game and your monitor. My ingame resolution is 2560x1440, while my monitor is at 3840x2160. The monitor resolution affects the pixel locations of all the clicking. i.e. when you read the code and you see a line like "pyautogui.click(702, 1323, duration=0.1)", then you should realize that this line shows the x-y location of "new game" in the main menu with respect to 3840x2160. If your monitor is at a different resolution, you have to scale ALL of the x-y numbers yourself, or you can use the reportMousePosition() function within the script by uncommenting it and commenting away playGame().

2. Likewise the ingame resolution affects the line "pyautogui.locateOnScreen(Door_path, confidence=0.9)", as this function might be sensitive to the exact number of pixels used for the door images in the "images" folder. If your character isn't opening the first door, and you've verified that openDoor() doesn't work, then you would have to recapture the door images on your own. You can do this by simply using print screen on your keyboard, pasting the image to MS Paint, then cropping out the door and saving it to that folder. There are likely to be 8-10 variations of the door based on my testing. This is also applicable to the "game_over" image.

3. Timing used for the sleep() function. If the script doesn't seem to run correctly, you might need to increase this value because your computer might not be as fast as mine. One of the biggest telltale signs is if you are being tabbed out and the Amplitude Studios website is opened, because this means that you have somehow clicked on Amplitude Studios logo at the bottom right of the screen. You'll have to observe the flow of the script to figure out where to adjust the delays. The code is not difficult to read, even if you have no prior experience with coding.

# Outro

I spent 3-4 hours coding and debugging this script and I spent around 20 hours opening the remaining 5300 doors in my case. Sounds like a pretty sweet deal considering I wasn't doing the clicking myself. Good luck with using the script!
