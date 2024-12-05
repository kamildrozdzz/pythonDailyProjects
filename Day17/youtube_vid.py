import os
import pyautogui
import time
import mouse

# Ścieżka do pliku
os.startfile(r'C:\Studia\5 sem\pythonProjects\pythonDailyProjects\Day16\test.txt')
time.sleep(1)  # Dłuższe opóźnienie na otwarcie pliku
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('Witam!', interval=0.1)
pyautogui.press('enter')
pyautogui.write('Przejalem wladze....', interval=0.1)
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 's')
pyautogui.hotkey('alt', 'f4')

# Przełączanie aplikacji
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('chrome', interval=0.1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('ctrl', 'l')
# Wpisywanie URL
pyautogui.write('www.youtube.com', interval=0.1)
pyautogui.press('enter')
time.sleep(3)
mouse.move(960,210)
mouse.click('left')
# Wpisywanie tekstu w YouTube
pyautogui.write('Never gonna give you up')
pyautogui.press('enter')
time.sleep(1)

mouse.move(900,320)
mouse.click('left')


# Kliknięcie lewym przyciskiem myszy

