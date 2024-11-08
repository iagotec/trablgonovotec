import pyautogui as pa #automação 
import pyperclip #copiar text
import time
import threading
import os
import keyboard

def click():
  while True:
    pa.click(835, y=433)
  
def encerrar():
  while True:
    if keyboard.is_pressed('q'):
      os._exit(0)
      break 



threading.Thread(target=click).start()
threading.Thread(target=encerrar).start()

while True:
  time.sleep(5)
  print(pa.position()) 

  