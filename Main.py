import os
import json
from datetime import datetime
import pywhatkit as pkit
import pyautogui
import time

CONFIG_FILE = "config.json"
HISTORY_FILE = "history.json"

with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    config = json.load(f)

with open(HISTORY_FILE, "r", encoding="utf-8") as h:
    history = json.load(h)

today_str = datetime.now().strftime("%d-%m-%Y")

days_so_far =  len(history.keys()) + 1

if days_so_far > 9:
    print("Campaign complete")
    exit()
else:
    if today_str in history:
        print("Campaign already sent today")
        exit()
    else:
        image_path = f'{config.get("Imagepath")}/image_{days_so_far}.jpg'
        caption = config["Messages"].get(str(days_so_far))
        if not os.path.exists(image_path):
            print(f"Image for day {days_so_far} not found at {image_path}")
            exit()

        else:
            try:
                pyautogui.alert(f"Sending image for day {days_so_far} to {config.get('Phone number')}. Please do not use your computer for the next 20 seconds.")
                pyautogui.hotkey('ctrl', 'alt', '/')
                time.sleep(1)
                pyautogui.write(config.get("Phone number"))
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(2)
                pkit.sendwhats_image(
                    config.get("Phone number"),
                      image_path,
                     caption,
                    wait_time=10,
                    close_time=5)
                print(f"Sent image for day {days_so_far} to {config.get('Phone number')}")
                history[today_str] = {"day": days_so_far, "status": "sent"}
                with open(HISTORY_FILE, "w") as h:
                    json.dump(history, h, indent=4)

            except Exception as e:
                print(f"something unexpected occurred at day {days_so_far}: {e}")