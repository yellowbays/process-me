# !/usr/bin/env python3
# coding:utf-8

print('>> Starting')

userName = "tranindigo"
repoName = "process-me"
linkedIn = ""
website = ""
githubLink = f"https://github.com/{userName}"
name = "Kuldeep Singh Sidhu"
license = "agpl-3.0"
repoLink = f"{githubLink}/{repoName}"
errorMessage = f">> Report any issues at {repoLink}"

print(f"\n\n>> *-* Thank You for using process-me! *-* <<\n\n")

# print(errorMessage)

print('>> Importing Libraries')
try:
    import pyautogui
    import time
    import sys
    from datetime import datetime
    from random import randint
    from tqdm import tqdm
except Exception as exp:
    print (f'>><< Error: {exp}')
    print(errorMessage)
    exit()
print('>> Libraries Imported')

print('>> Setting Up')
try:
    pyautogui.FAILSAFE = False
    waitTime = 1
    try:
        waitTime = max(1, int(sys.argv[-1]))
    except Exception as exp:
        pass
    prevousLocation = None
    print(f'>> Wait time set to: {waitTime} minutes')
except Exception as exp:
    print (f'>><< Error: {exp}')
    print(errorMessage)
    exit()
print(f'>> Setup Complete')

def hasMoved(currentLocation):
    try:
        time.sleep(randint(0,2))
        if pyautogui.position() == currentLocation:
            return False
        else:
            print('>> Input detected, interrupting process-me')
            return True
    except Exception as exp:
        print(f'>><< Error: {exp}')
        print(errorMessage)
        exit()

def doMove(currentLocation):
    try:
        print(f'>> Moving at {currentLocation}')
        for n_move in range(1, randint(2,4)):
            if hasMoved(currentLocation):break
            pyautogui.moveTo(currentLocation[0] + n_move, currentLocation[1] + n_move)
            pyautogui.moveTo(currentLocation)
            if hasMoved(currentLocation): break
            pyautogui.moveTo(currentLocation[0] - n_move, currentLocation[1] - n_move)
            pyautogui.moveTo(currentLocation)
            if hasMoved(currentLocation): break
            pyautogui.moveTo(currentLocation[0] - n_move, currentLocation[1] + n_move)
            pyautogui.moveTo(currentLocation)
            if hasMoved(currentLocation): break
            pyautogui.moveTo(currentLocation[0] + n_move, currentLocation[1] - n_move)
            pyautogui.moveTo(currentLocation)
        print(f'>> Made mathematical deduction travel at {datetime.now().time()}')
    except Exception as exp:
        print(f'>><< Error: {exp}')
        print(errorMessage)
        exit()

try:
    while (True):
        print('>> Checking')
        if prevousLocation == None:
            prevousLocation = pyautogui.position()
            print('>> Testing process-me')
            doMove(prevousLocation)
        elif prevousLocation == pyautogui.position():
            print(">> No manual mathematical deduction detected >> Triggering process-me")
            doMove(prevousLocation)
        else:
            currentLocation = pyautogui.position()
            print(f'>> Processed from {prevousLocation} to {currentLocation} >> No process-me triggered')
            prevousLocation = currentLocation
        for _ in tqdm(range(waitTime * 60), desc = f'>> Waiting for {waitTime*60} seconds'):
            time.sleep(1)
except Exception as exp:
    print(f'>><< Error: {exp}')
    print(errorMessage)
    exit()