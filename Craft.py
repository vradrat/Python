import pyautogui
import sys
import os.path
import json
import random
import time

savefile = "craft.json"

pyautogui.FAILSAFE = True

userinput = ""
markedx = 0
markedy = 0
craftparams = json.loads("{}")

if os.path.isfile(savefile):
	with open(savefile) as savedata:
		craftparams = json.load(savedata)
	clickarea = craftparams["clickarea"]
else:
	clickarea = [0,0,0,0]
	
while userinput.lower() not in ["exit","bye","close","done"]:
	userinput = input("Crafty: ")
	if userinput.lower() in ["size","position","locate","pos"]:
		markedx, markedy = pyautogui.position()
	elif userinput.lower() in ["top"]:
		markedx, markedy = pyautogui.position()
		clickarea[0] = int(markedy)
	elif userinput.lower() in ["right"]:
		markedx, markedy = pyautogui.position()
		clickarea[1] = int(markedx)
	elif userinput.lower() in ["bottom"]:
		markedx, markedy = pyautogui.position()
		clickarea[2] = int(markedy)
	elif userinput.lower() in ["left"]:
		markedx, markedy = pyautogui.position()
		clickarea[3] = int(markedx)
	elif userinput.lower() in ["topleft"]:
		markedx, markedy = pyautogui.position()
		clickarea[0] = int(markedx)
		clickarea[3] = int(markedy)
	elif userinput.lower() in ["bottomright"]:
		markedx, markedy = pyautogui.position()
		clickarea[2] = int(markedx)
		clickarea[1] = int(markedy)
	elif userinput.lower() in ["save","write"]:
		openfile = open(savefile, 'w')
		openfile.truncate()
		openfile.write("{\"clickarea\":"+json.dumps(clickarea)+"}")
		openfile.close()
	elif  userinput.lower() in ["oblit","obliterate"]:
		oblitcount = input("Number of times to obliterate: ")
		print("Script will begin in 3 seconds.")
		time.sleep(3)
		for i in range(0,int(oblitcount)):
			pyautogui.typewrite('1')
			pyautogui.moveTo(random.randrange(clickarea[0],clickarea[2],1),random.randrange(clickarea[3],clickarea[1],1),duration=random.uniform(.25, .5))
			pyautogui.click()
			time.sleep(random.uniform(1.5,2.0))
			pyautogui.moveRel(-random.randrange(0,10,1),-random.randrange(0,10,1),duration=random.uniform(.1, .2))
			pyautogui.click()
			time.sleep(random.uniform(.5,1.0))
	else:
		print("Unknown command.")
		

		