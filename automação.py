import pyautogui as pa #automação 
import pyperclip #copiar text
import time


#procurar arquivo  
pa.press('win')
pa.sleep(1)
pyperclip.copy('esplorador de arquivos')
pa.sleep(1)

pa.hotkey('ctrl', 'v')
pa.sleep(1)

pa.click(x=183, y=585)
pa.sleep(1)

pa.press('f11')
pa.sleep(1)

pa.hotkey('ctrl','f')
pyperclip.copy('trabalho escola')
pa.hotkey('ctrl', 'v')
pa.sleep(1)
pa.click(x=324, y=67, clicks=2, interval=0.1)
pa.sleep(1)

#cadastro
pa.click(x=958, y=620)
pa.sleep(3)

#nome
pa.click(x=961, y=451)
pyperclip.copy('Vinicius Varia')
pa.hotkey('ctrl', 'v')


#email
pa.click(x=845, y=500)
pyperclip.copy('viniciusbaessi@gmail.com')
pa.hotkey('ctrl', 'v')


#cpf
pa.click(x=882, y=545)
pyperclip.copy('12345678900')
pa.hotkey('ctrl', 'v')

#senha
pa.click(x=871, y=611)
pyperclip.copy('123456')
pa.hotkey('ctrl', 'v')

#senha
pa.click(x=883, y=652)
pyperclip.copy('123456')
pa.hotkey('ctrl', 'v')
pa.sleep(2)

pa.click(x=834, y=676)







while True:
  time.sleep(5)
  print(pa.position()) 