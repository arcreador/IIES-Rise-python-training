
import os




while True:
	print("chat with me with your requirements : "  , end='')
	p = input()

	if ("not" in p) or ("never" in p) or ("didn't" in p) or ("don't" in p) or ("doen't" in p):
	  print("okay Sure! Anything else")

	elif (("start" in p) or ("run" in p ))  and ("chrome" in p):
	  os.system("chrome")

	elif (("run" in p) or  ("execute" in p ) or ("start" in p ) ) and  (("notepad" in p) or ("editor" in p) ) :
	  os.system("notepad")

	elif (("start" in p) or ("run" in p ))  and ("player" in p) and ("media" in p):
	  os.system("wmplayer")

	elif (("start" in p) or ("run" in p)) and ("paint" in p):
	  os.system("mspaint")  		

	elif (("start" in p) or ("run" in p)) and ("vlc" in p):
	  os.system("vlc") 
	
	elif  ("exit" in p)  or ("quit" in p) or ("end" in p):
	  break

	else:
	  print("dont support")


