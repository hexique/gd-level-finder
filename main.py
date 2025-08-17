import requests
import json
from random import randint
from time import gmtime, strftime, sleep
from colorama import Fore

# thx to tttn324 for fetchGJLevel() and fetchGJPage()

TIMEOUT = 0.53 # Timeout to fetch GJ Levels (seconds)
MINIMAL_ID = 97454629 # Lowest possible level ID (default - 97454629, First 2.2 level)

def fetchGDBrowser(level_id):
    url = f"https://gdbrowser.com/api/level/{level_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()

        # print(data)
        return data
    
    except requests.exceptions.RequestException as e:
        # print(f'Failed to find level {level_id}')
        return
    except json.JSONDecodeError:
        print(response)
        return

def getGJPage(type=0, str="", page=0, diff=None, demonFilter=None, len0=None, accountID=None, epic=0, mythic=0):
    data = {
        "str": str,
        "type": type,
        "page": page,
        "secret": "Wmfd2893gb7",
        "mythic": mythic,
        "epic": epic
    }
    if accountID is not None:
        data["accountID"]=accountID
    if diff is not None:
        data["diff"]=diff
    if demonFilter is not None:
        data["demonFilter"]=demonFilter
    if len0 is not None:
        data["len"]=len0
    try:
        req = requests.post(url="http://www.boomlings.com/database/getGJLevels21.php", data=data, headers={"User-Agent": ""})
        return req.text
    except Exception as e:
        print(e)
        return
    
def fetchGJLevel(id):
    # print(f'{Fore.BLACK}fetching GJ Level {id}...')
    sleep(TIMEOUT)
    try:
        return requests.post(url="http://www.boomlings.com/database/downloadGJLevel22.php", data={"levelID": id,"secret": "Wmfd2893gb7"}, headers={"User-Agent": ""}).text
    except Exception as e:
        return

def save(result):
    try:
        with open(f"logs\\log {launch_time}.json", "w", encoding="UTF-8") as f:
            json.dump(result, f, indent=4)
    except FileNotFoundError:
        print(f'{Fore.RED}Directory \'logs\' not found, writing at {launch_time}.json')
        with open(f"log {launch_time}.json", "w", encoding="UTF-8") as f:
            json.dump(result, f, indent=4)
launch_time = strftime("%m-%d %H-%M-%S", gmtime())
print(f'Result will appear at \'logs/log {launch_time}.json\'')

try:
    with open("params.json", "r", encoding="UTF-8") as f:
        params = json.load(f)
except FileNotFoundError:
    if input("Do you want to save 'Friends Only' levels? (y/n)\n").lower().strip() == "y":
        params = {"friends-only": True}
    else:
        params = {"friends-only": False}
    with open("params.json", "w", encoding="UTF-8") as f:
        json.dump(params, f)

last_lvl_id = int(getGJPage(4).split(":")[1])
result = []

i = 0
while True:
    id = randint(MINIMAL_ID, last_lvl_id)
    gd_browser_info = fetchGDBrowser(id)
    gj_info = fetchGJLevel(id)
    # print(gj_info)
    i += 1
    if gj_info == None:
        print(f"{Fore.RED}{i}. Level {id} is not found.")
    elif gd_browser_info == None and gj_info == "-1":
        print(f"{Fore.YELLOW}{i}. Level {id} is unlisted (Friends only).")
        result.append({"ID": id, "GJInfo": gj_info, "Type": "Friends only"})

    elif gd_browser_info == None and gj_info != "-1":
        print(f"{Fore.GREEN}{i}. Level {id} is unlisted.")

        
        result.append({"ID": id, "GJInfo": gj_info, "Type": "Unlisted"})
        save(result)
    elif gd_browser_info != None:
        print(f"{Fore.BLACK}{i}. Level {id} is not unlisted.")
