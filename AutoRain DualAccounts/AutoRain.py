import os, time, cloudscraper, pyautogui, random, subprocess, json, threading, pynput, pyperclip
from win10toast import ToastNotifier
from playsound import playsound
from termcolor import cprint
os.system('cls')
try:
  with open("config.json", "r") as config:
    config = json.load(config)
except:
  cprint("config.json file is missing. Make sure you downloaded all the files and config is in the same folder","red")
  time.sleep(5)
  cprint("Exiting...","yellow")
  time.sleep(0.3)
  quit()

storage = []
scraper = cloudscraper.create_scraper()
auth = config['main_account_bloxflip_token']
token = config['key']
join_sound = config['RainJoinSound']
minimum_prize = config['minimum_amount']
disabledcontrols = config['disabled_controls']
token1 = config['bloxflip_token1']
safehop = config['safe_hop_accounts']
oneaccount = config['one_account']
toast = ToastNotifier()
cprint("[CREDITS:] AutoRain made by Thwartedbrute#8188","cyan")
time.sleep(5)
os.system('cls')
token = len(token)

try:
  get = scraper.get("https://rest-bf.blox.land/user", headers = {"origin": "https://bloxflip.com", "x-auth-token": auth})
  info = get.json()['user']
  cprint(f"Logged in as {info['robloxUsername']}\nCurrent balance: {info['wallet']}\n","cyan")
  if oneaccount == False:
    get = scraper.get("https://rest-bf.blox.land/user", headers = {"origin": "https://bloxflip.com", "x-auth-token": token1})
    info = get.json()['user']
    cprint(f"Logged in as {info['robloxUsername']}\nCurrent balance: {info['wallet']}\n","cyan")
  else:
    time.sleep(0)
except:
  cprint("Invalid Auth Token. Open the README file and follow the directions to get your BloxFlip Token","red")
  time.sleep(5)
  cprint("Exiting...","yellow")
  time.sleep(0.3)
  quit()

if disabledcontrols == True:
  cprint("Disabled Controls is enabled. This means you cannot move your mouse or keyboard. You can disable this in config.\nalso make sure to put this application in a good area as you wont be able to move it later.","yellow")
  enable = input("type yes to continue.\n")
  if enable == 'yes':
    mouse_listener = pynput.mouse.Listener(suppress=True)
    mouse_listener.start()
    keyboard_listener = pynput.keyboard.Listener(suppress=True)
    keyboard_listener.start()
  else:
    cprint("Exiting...","red")
    time.sleep(0.3)
    quit()

if token == 95:
  cprint("AutoRain Enabled! Press Ctrl + C to exit.","magenta")
  while True:
    try:
      r = scraper.get('https://rest-bf.blox.land/chat/history').json()
      check = r['rain']
      if check['active'] == True:
        if check['prize'] >= minimum_prize:
          store = scraper.get("https://rest-bf.blox.land/user", headers = {"x-auth-token": f"{auth}"}).json()['user']['wallet']
          storage.append(store)
          grabprize = str(check['prize'])[:-2]
          prize = (format(int(grabprize),","))
          host = check['host']
          getduration = check['duration']
          convert = (getduration/(1000*60))%60
          duration = (int(convert))
          waiting = (convert*60+10)
          sent = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(int(time.time())))
          time.sleep(1)
          while True:
            x = random.randint(1,500)
            y = random.randint(1,500)
            join = pyautogui.locateCenterOnScreen('assets/pro.png', confidence = 0.9)
            if join:
              if disabledcontrols == True:
                mouse_listener.stop()
                keyboard_listener.stop()
              time.sleep(2)
              pyautogui.moveTo(join)
              time.sleep(0.5)
              pyautogui.click()
              time.sleep(2)
              pyautogui.moveTo(x, y, 0.5)
              if disabledcontrols == True:
                time.sleep(1)
                mouse_listener = pynput.mouse.Listener(suppress=True)
                mouse_listener.start()
                keyboard_listener = pynput.keyboard.Listener(suppress=True)
                keyboard_listener.start()
            if not join:
              cprint("Could not locate join button, opening bloxlfip...", "red")
              subprocess.call("start https://bloxflip.com",shell=True)
              if disabledcontrols == True:
                mouse_listener.stop()
                keyboard_listener.stop()
              time.sleep(10)
              join = pyautogui.locateCenterOnScreen('assets/pro.png', confidence = 0.9)
              pyautogui.moveTo(join)
              time.sleep(0.5)
              pyautogui.click()
              time.sleep(2)
              pyautogui.moveTo(x, y, 0.5)
              if disabledcontrols == True:
                time.sleep(1)
                mouse_listener = pynput.mouse.Listener(suppress=True)
                mouse_listener.start()
                keyboard_listener = pynput.keyboard.Listener(suppress=True)
                keyboard_listener.start()
            if oneaccount == False:
              time.sleep(30)
              account1 = f"localStorage.setItem('_DO_NOT_SHARE_BLOXFLIP_TOKEN', '{token1}'); location['reload']();"
              pyperclip. copy(account1)
              if safehop == True:
                time.sleep(0.2)
              pyautogui.hotkey('ctrl', 'l')
              if safehop == True:
                time.sleep(0.2)
              pyautogui.write("javascript:")
              if safehop == True:
                time.sleep(0.2)
              pyautogui.hotkey('ctrl', 'v')
              if safehop == True:
                time.sleep(0.2)
              pyautogui.hotkey('enter')
              time.sleep(10)
              x = random.randint(1,500)
              y = random.randint(1,500)
              join = pyautogui.locateCenterOnScreen('assets/pro.png', confidence = 0.9)
              if join:
                if disabledcontrols == True:
                  mouse_listener.stop()
                  keyboard_listener.stop()
                time.sleep(2)
                pyautogui.moveTo(join)
                time.sleep(0.5)
                pyautogui.click()
                time.sleep(2)
                pyautogui.moveTo(x, y, 0.5)
                time.sleep(30)
                account = f"localStorage.setItem('_DO_NOT_SHARE_BLOXFLIP_TOKEN', '{auth}'); location['reload']();"
                pyperclip. copy(account)
                if safehop == True:
                  time.sleep(0.2)
                pyautogui.hotkey('ctrl', 'l')
                if safehop == True:
                  time.sleep(0.2)
                pyautogui.write("javascript:")
                if safehop == True:
                  time.sleep(0.2)
                pyautogui.hotkey('ctrl', 'v')
                if safehop == True:
                  time.sleep(0.2)
                pyautogui.hotkey('enter')
                if disabledcontrols == True:
                  time.sleep(1)
                  mouse_listener = pynput.mouse.Listener(suppress=True)
                  mouse_listener.start()
                  keyboard_listener = pynput.keyboard.Listener(suppress=True)
                  keyboard_listener.start()
              if not join:
                cprint("Could not locate join button, opening bloxlfip...", "red")
                subprocess.call("start https://bloxflip.com",shell=True)
                if disabledcontrols == True:
                  mouse_listener.stop()
                  keyboard_listener.stop()
                time.sleep(10)
                join = pyautogui.locateCenterOnScreen('assets/pro.png', confidence = 0.9)
                pyautogui.moveTo(join)
                time.sleep(0.5)
                pyautogui.click()
                time.sleep(2)
                pyautogui.moveTo(x, y, 0.5)
                time.sleep(30)
                account = f"localStorage.setItem('_DO_NOT_SHARE_BLOXFLIP_TOKEN', '{auth}'); location['reload']();"
                pyperclip. copy(account)
                if safehop == True:
                  time.sleep(0.2)
                pyautogui.hotkey('ctrl', 'l')
                if safehop == True:
                  time.sleep(0.2)
                pyautogui.write("javascript:")
                if safehop == True:
                  time.sleep(0.2)
                pyautogui.hotkey('ctrl', 'v')
                if safehop == True:
                  time.sleep(0.2)
                pyautogui.hotkey('enter')
                if disabledcontrols == True:
                  time.sleep(1)
                  mouse_listener = pynput.mouse.Listener(suppress=True)
                  mouse_listener.start()
                  keyboard_listener = pynput.keyboard.Listener(suppress=True)
                  keyboard_listener.start()                      
            break
          info = scraper.get("https://rest-bf.blox.land/user", headers = {"x-auth-token": f"{auth}"}).json()['user']
          checker = scraper.get("https://rest-bf.blox.land/chat/history").json()['rain']['players']
          if join_sound == True:
            threading.Thread(target=playsound, args=('assets\Win.mp3',)).start()
          cprint(f"Successfully joined rain!","green")
          cprint(f"Account: {info['robloxUsername']}","yellow")
          cprint(f"Rain amount: {prize} R$", "cyan")
          cprint(f"Expiration: {duration} minutes","yellow")
          cprint(f"Host: {host}","yellow")
          cprint(f"Timestamp: {sent}","magenta")
          cprint(f"Current balance: {info['wallet']}\n","green")
          if oneaccount == False:
            info = scraper.get("https://rest-bf.blox.land/user", headers = {"x-auth-token": f"{token1}"}).json()['user']
            cprint(f"Successfully joined rain on alt!","green")
            cprint(f"Account: {info['robloxUsername']}","yellow")
            cprint(f"Current balance: {info['wallet']}\n","green")
          time.sleep(waiting)
      elif check['active'] == False:
        time.sleep(5)
    except Exception:
      time.sleep(5)
else:
  cprint("Invalid key! To buy a valid key create a ticket in the discord server or Message Thwartedbrute#8188. https://discord.gg/AUKrqq8tcF", "red")
  time.sleep(5)
  cprint('Exiting...','yellow')
  time.sleep(0.3)
  quit()