import pyautogui
from cryptography.fernet import Fernet
import sys
import getpass
import base64
import time
import win32gui

passfile = "pashash"
userfile = "usrhash"
keyfile = "keyhash"
keylock = b'GKxxq9TX4UfsFsWUreyv5OvSKNKrH4Lnuk0JqZta4BQ='

def getcred():
  openfile = open(keyfile,'rb')
  tokenkey = openfile.read()
  openfile.close()
  openfile = open(userfile,'rb')
  tokenuser = openfile.read()
  openfile.close()
  openfile = open(passfile,'rb')
  tokenpass = openfile.read()
  openfile.close()
  g = Fernet(keylock)
  key = g.decrypt(tokenkey)
  f = Fernet(key)
  username = str(f.decrypt(tokenuser),'utf-32')
  password = str(f.decrypt(tokenpass),'utf-32')
  return (username,password)

if len(sys.argv) > 1:
  if "s" in sys.argv or "S" in sys.argv or "-s" in sys.argv or "-S" in sys.argv:
    print("Input your username and password. \n")
    username = bytes(input("User name: ").strip(), "utf-32")
    password = bytes(getpass.getpass("Password: ").strip(), "utf-32")
    key = Fernet.generate_key()
    f = Fernet(key)
    g = Fernet(keylock)
    tokenuser = f.encrypt(username)
    tokenpass = f.encrypt(password)
    tokenkey = g.encrypt(key)
    openfile = open(userfile, 'w')
    openfile.truncate()
    openfile.write(str(tokenuser)[2:-1])
    openfile.close()
    openfile = open(passfile, 'w')
    openfile.truncate()
    openfile.write(str(tokenpass)[2:-1])
    openfile.close()
    openfile = open(keyfile, 'w')
    openfile.truncate()
    openfile.write(str(tokenkey)[2:-1])
    openfile.close()
    print(f.decrypt(tokenpass))
  elif "p" in sys.argv or "P" in sys.argv or "-p" in sys.argv or "-P" in sys.argv:
    username, password = getcred()
    #pyautogui.typewrite(password)
    
else:
  time.sleep(2)
  x = win32gui.GetForegroundWindow()
  #x = 524822
  #print(str(x))
  win32gui.SetActiveWindow(x)
  win32gui.SetForegroundWindow(x)
  username, password = getcred()
  time.sleep(.1)
  #pyautogui.typewrite(username)
  #pyautogui.press('tab')
  time.sleep(.1)
  #pyautogui.typewrite(password)
  pyautogui.typewrite("1")
  y = input("All done.")