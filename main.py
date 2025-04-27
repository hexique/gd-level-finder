import requests
import json
from random import randint

def get_info(level_id):
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

def get_info_author(author, page):
    url = f"https://gdbrowser.com/api/search/{author}?page={page}&count=10&user"

    try:
        response = requests.get(url)
        response.raise_for_status()

        # print(response)
        levels = response.json()

        # print(levels)
        result = [i['id'] for i in levels]
        return (result, levels)

    except requests.exceptions.RequestException as e:
        print(f'Failed to find level {e}\nResponse: {response}\nAuthor: {author}\nLevel: {level["id"]}')
        return
    except json.JSONDecodeError:
        print(response.json())
        return

while True:
    level = None
    while True:
        level = get_info(randint(128, 117979939))
        if level != None:

            level_author = get_info_author(level['author'], 0)
            if level_author == None:
                continue
            level_author = level_author[1]
            levels=[]
            for i in range(int(level_author[0]['pages'])):
                levels.extend(get_info_author(level['author'], i)[0])

            if level['id'] not in levels:
                print(level['id'], levels)
                break
            else:
                pass
                # print(f"PUBLIC {level['name']} by {level['author']}\nLikes: {level['likes']}\nDownloads: {level['downloads']}\nObjects: {level['objects']}\nLen: {len(levels)}\n{level['id']}\n")

    print(f"!!!\n\n{level['name']} by {level['author']}\nLikes: {level['likes']}\nObjects: {level['objects']}\nLen: {len(levels)}\nDownloads: {level['downloads']}\n{level['id']}\n\n!!!")
    print()
    # input()