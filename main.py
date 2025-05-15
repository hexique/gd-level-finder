import requests
import json
from random import randint
from time import ctime

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

# while True:
#     level = None
#     while True:
#         level = get_info(randint(128, 117979939))
#         if level != None:

#             level_author = get_info_author(level['author'], 0)
#             if level_author == None:
#                 continue
#             level_author = level_author[1]
#             levels=[]
#             for i in range(int(level_author[0]['pages'])):
#                 levels.extend(get_info_author(level['author'], i)[0])

#             if level['id'] not in levels:
#                 print(level['id'], levels)
#                 break
#             else:
#                 pass
#                 # print(f"PUBLIC {level['name']} by {level['author']}\nLikes: {level['likes']}\nDownloads: {level['downloads']}\nObjects: {level['objects']}\nLen: {len(levels)}\n{level['id']}\n")

# i = 118026371
# for j in range(10000):
#     i -= 1
#     level = get_info(i)
#     if level != None:
#         if level['author'] == 'Tttn324':
#             print(f"LESSS GO WE FIND ID\n\n{level['name']} by {level['author']}\nLikes: {level['likes']}\nObjects: {level['objects']}\nDownloads: {level['downloads']}\n{level['id']}\n\n")
#             break
#         print(f"{level['name']} by {level['author']}\nLikes: {level['likes']}\nObjects: {level['objects']}\nDownloads: {level['downloads']}\n{level['id']}\n\n!!!")

data = {}
data_cl = {}
exist_levels = []

with open('data.json', 'r', encoding='utf-8') as f:
    file = f.read()
    data = json.loads(file)
    print(f'Data successfully loaded (len is {len(data.keys())})')

with open('data-new.json', 'r', encoding='utf-8') as f:
    file = f.read()
    data_cl = json.loads(file)
    print(f'Data new successfully loaded (len is {len(data_cl.keys())})')

with open('exist_levels.json', 'r', encoding='utf-8') as f:
    file = f.read()
    exist_levels = json.loads(file)
    print(f'Exist levels successfully loaded (len is {len(exist_levels)})')


with open('data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps({**data, **data_cl}))
    print(f'Data and data new successfully merged (len is {len(data.keys()) + len(data_cl.keys())})')
with open('data-new.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps({}))

old_data_len = len(data.keys()) + len(data_cl.keys())
data_cl = {}

while True:
    try:
        id = randint(128, 118028738)
        if str(id) in data.keys() or id in data_cl.keys():
            print(f'ID {id} is already exist')
            exist_levels.append(id)
            with open('exist_levels.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(exist_levels))
            continue
        level = get_info(id)
        if level != None:
            data_cl[level['id']] = level
            with open('data-new.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(data_cl))
            print(f'\nData length: {len(data_cl.keys()) + old_data_len} ({len(data_cl.keys())})\n')
            print(f"""[{ctime()}]\n{level['name']} by {level['author']}
        
Likes: {level['likes']}
Downloads: {level['downloads']}
Objects: {level['objects']}
Version: {level['gameVersion']}
{level['id']}
    """)
        else:
            data_cl[id] = None
            print(f'ID {id} is not exist')
    except Exception as e:
        print(ctime(), e)
    # input()