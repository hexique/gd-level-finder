import json
from time import time
from random import shuffle, choice
from colorama import *

paths = ('D:\projects\py\\tkinter\Crypta\GD-Level-Scan\\data (compressed + index).json',
         'D:\projects\py\\tkinter\Crypta\GD-Level-Scan\\data (sorted).json', 'D:\projects\py\\tkinter\Crypta\data.json', 'D:\projects\py\\tkinter\Crypta\data-temp.json', 
         'D:\projects\py\\tkinter\Crypta\GD-Level-Scan\\data.json', 'D:\projects\py\\tkinter\Crypta\GD-Level-Scan\\data-temp.json',
         'D:\projects\py\\tkinter\Crypta\GD-Level-Scan\\data 1.json', 'D:\projects\py\\tkinter\Crypta\GD-Level-Scan\\data (raw).json', 
         'D:\projects\py\\tkinter\Crypta\GD-Level-Scan\\data (compressed).json', 'D:\projects\py\\tkinter\Crypta\GD-Level-Scan\\data (cropped 1951420).json'
         )

idToDate = {
    "1.0": 2172,
    "1.1": 13794,
    "1.2": 61916,
    "1.3": 74634,
    "1.4": 181913,
    "1.5": 417148,
    "1.6": 825973,
    "1.7": 1286694,
    "1.8": 2804282,
    "1.9": 11010134,
    "2.0": 28315639,
    "2.1": 97426239,
    "2.2": 118028739
}

yearToDate = {
    "2013": 130629,
    "2014": 3938229,
    "2015": 15435856,
    "2016": 27788667,
    "2017": 40559842,
    "2018": 51591727,
    "2019": 58976287,
    "2020": 66144272,
    "2021": 77026243,
    "2022": 87321749,
    "2023": 98379505,
    "2024": 113708332,
    "2025": 118028739

}

def read_json(path):
    print('reading ' + path.split("\\")[-1] + '...')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    print(path.split("\\")[-1] + ' is successfully read')
    return data

def remove_undefined(path: str, isLast: bool):
    with open(path, 'r', encoding='utf-8') as f:
        data: dict = json.load(f)
    i = 0
    if isLast:
        keys = list(data.keys())[::-1]
        while data[keys[0]] == None:
            i += 1
            del data[keys[0]]
            print(f'{i}. Removed {keys[0]}')
            del keys[0]
        else:
            print(f'Successfully removed {i} levels')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(json.dumps(data))
    else:
        keys = list(data.keys())[::-1]
        cache = []
        undefined_counter = 0
        while undefined_counter < 100:
            i += 1
            if data[keys[0]] == None:
                undefined_counter += 1
                print(f'Total undefined levels: {undefined_counter}. Total scaned {i}')
                cache.append(keys[0])
                del keys[0]
            else:
                print(f'Level {keys[0]} is exists')
                undefined_counter = 0
                del keys[0]
        else:
            print(f'found undefined levels at position {keys[0]}')
            for level in cache:
                del data[level]



def count_length(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    undefined_levels = 0
    
    for i in data.keys():
        if data[i] == None:
            undefined_levels += 1
    return (len(list(data.keys())), undefined_levels)
    
def create_backup(path: str):

    with open(path, 'r', encoding='utf-8') as f:
        data: dict = json.load(f)
    path = '\\'.join(path.split('\\')[0:-1]) + f'\\data ({len(data.keys())}).json'
    print(path)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data))

    # with open(path, 'w', encoding='utf-8') as f:
    #     data: dict = json.load(f)

def validate(path: str):
    data = read_json(path)
    # i = 0
    # print(data[-1])
    # while data[-1] != '}':
    #     i += 1
    #     data = data[:-1]
    #     print(i, data[-1])
    # else:
    #     print(i, data[-1], 'x')


    with open(path.replace('.json', ' (valid).json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def merge(*args):
    with open(args[0], 'r', encoding='utf-8') as f:
        first_data = json.loads(f.read())
    print(f'{args[0]} is loaded')
    with open(args[1], 'r', encoding='utf-8') as f:
        second_data = json.loads(f.read())
    print(f'{args[1]} is loaded')
    with open(args[0].replace('.json', f' (merged).json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps({**first_data, **second_data}))

def format(path: str):
    print(f'loading {path}...')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    print(f'{path} is succesfully loaded')

    formated_data = []

    i = 0
    for level in data:
        if data[level] is None:
            continue
        for key in ("partialDiff", "difficultyFace", "disliked", "featured", "epic", "legendary", "mythic", "epicValue", "editorTime", "totalEditorTime", "ldm"):
            data[level].pop(key)
        for versionId in list(idToDate.keys()):
            if int(level) < idToDate[versionId]:
                uploadGameVersion = versionId
                break
        i += 1
        result = {**data[level], "index": i, "uploadGameVersion": uploadGameVersion}
        formated_data.append(result)
        print(result['name'], ':', result['uploadGameVersion'], result['index'])

    with open(path.replace(".json", "(formated).json"), 'w', encoding='utf-8') as f:
        f.write(json.dumps(formated_data))

def find(path):
    data = read_json(path)
    result = []

    lst = list(data.keys())
    print(len(lst))

    for level in data:
        break
        
        if abs(level["likes"]) - level["downloads"] < 0:
            result.append(level)



def sort(path):
    data = read_json(path)
    with open(path.replace(".json"," (sorted).json"), 'w', encoding='utf-8') as f:
        print('writing...')
        f.write(json.dumps(sorted(data, key=lambda item: int(item["id"]))))
    print('successfully writed')

def statByYear(data, year):
    result = {}
    # Insert your conditions here
    for level in data:
        if int(level["id"]) > yearToDate[year]:
            break
        for word in level["description"].split():
            if word in result:
                result[word] += 1
            else:
                result[word] = 1

    with open(f'GD-Level-Scan/stats/description-words-{year}.json', 'w', encoding='utf-8') as f:
        print('writing...')
        json.dump(dict(sorted(result.items(), key=lambda item: item[1], reverse=True)), f, indent=4)
    print('successfully writed')

def stat(path):
    data = read_json(path)
    
    result = {}
    # Insert your conditions here
    for level in data:
        for word in level["description"].split():
            if word in result:
                result[word] += 1
            else:
                result[word] = 1

    with open(f'GD-Level-Scan/stats/description-words.json', 'w', encoding='utf-8') as f:
        print('writing...')
        json.dump(dict(sorted(result.items(), key=lambda item: item[1], reverse=True)), f, indent=4)
    print('successfully writed')


def count(path):
    data = read_json(path)

    data = sorted(data, key=lambda item: int(item[0]))

    result = []

    counter = 0
    for level in data:

        # insert your conditions here
        if level["name"].lower().startswith('make your'):
            print(level["name"], ':', level["id"])
            counter += 1
    
    print(f'\nTotal found {counter} levels')

def find_unlisted(path):
    data = read_json(path)

    while True:
        total = 0
        unlisted = 0
        author = input("Enter an author or user ID:\n")
        if author.isnumeric():
            searchKey = "playerID"
        else:
            searchKey = "author"
        for level in data:
            if level[searchKey].lower() == author.lower():
                if level["accountID"] == "0": continue
                total += 1
                og_author = level["author"]
                if level["downloads"] < 25:
                    unlisted += 1
                    print(f'Found potentially unlisted level:   {level["name"]} ({level["downloads"]} downloads)\n{level["id"]}')
                else:
                    print(f'{Fore.BLACK}Trying:   {level["name"]} ({level["downloads"]} downloads)\nID: {level["id"]}{Fore.WHITE}')
        print(f'\nCompleted result for {og_author}\nTotal found {total} levels and {unlisted} potentially unlisted levels.\n')

def crop(path):
    data = read_json(path)
    shuffle(data)

    result = []
    length = int(input("Type a length of output JSON:\n"))
    i = 0
    for level in data:
        result.append(level)
        i += 1
        if i > length:
            break
    result = sorted(result, key=lambda item: int(item["id"]))

    i = 0
    for level in result:
        level["index"] = i
        i += 1

    with open(f'GD-Level-Scan/data (cropped {length}).json', 'w', encoding='utf-8') as f:
        print('writing...')
        json.dump(result, f)
    print('successfully writed')

def compress(path):
    data = read_json(path)
    for level in data:
        for key in ('orbs', 'diamonds', 'large'):
            level.pop(key)

    with open(f'GD-Level-Scan/data (compressed).json', 'w', encoding='utf-8') as f:
        print('writing...')
        json.dump(data, f)
    print('successfully writed')

def split_json(path):

    splited_len = int(input('Type number of parts:\n'))
    data = read_json(path)[:1951420]
    print(len(data))
    splited_len = len(data) // splited_len

    temp_data = [[]]
    for level in data:
        temp_data[-1].append(level)
        if len(temp_data[-1]) > splited_len:
            temp_data.append([])

    i = 0
    for file in temp_data:
        with open(f'GDLS\\data\\data {i}.json', 'w', encoding='utf-8') as f:
            print(f'writing data {i}...')
            json.dump(file, f)
        i += 1
        print('successfully writed')

def format_index(path):

    data = read_json(path)

    i = 0
    for level in data:
        level["index"] = i
        i += 1

    with open(f'GD-Level-Scan\\data (index).json', 'w', encoding='utf-8') as f:
        print(f'writing data...')
        json.dump(data, f, indent=4)
    
    for level in data:
        for key in ('orbs', 'diamonds', 'large'):
            level.pop(key)

    with open(f'GD-Level-Scan\\data (compressed + index).json', 'w', encoding='utf-8') as f:
        print(f'writing compressed data...')
        json.dump(data, f)
    
def calculate_difference(path):
    data = read_json(path)

    # result = []

    # audit = ''
    # for i in range(1, len(data)):
    #     result.append(int(data[i]["id"]) - int(data[i-1]["id"]))
    #     audit += f'{i}. {result[-1]} | {sum(result) / len(result)}\n'
    # print(f'{i}. {result[-1]} | {sum(result) / len(result)}')

    # with open(f'GD-Level-Scan\\differences.txt', 'w', encoding='utf-8') as f:
    #     print(f'writing data...')
    #     f.write(audit)
    for level in data:
        pass

def display_group(path):
    data = read_json(path)
    data = dict(sorted(data.items(), key=lambda item: int(item[0]), reverse=0))


    i = 0
    exist = 0
    nonexist = 0
    for level in data.keys():
        i += 1
        if data[level] != None:
            print(f'{level}: {data[level]["name"]} by {data[level]["author"]}')
            exist += 1
        else:
            print(f'{level}: {data[level]}')
            nonexist += 1
        if data[level] is not None:
            if int(data[level]["id"]) > 25050: break
    print(exist, nonexist, exist + nonexist)

def display_version(path):
    data = read_json(path)
    i = 0
    for level in data:
        i += 1
        if level["uploadGameVersion"] == "1.0":
            print(f'{i}. {level["name"]} by {level["author"]}\n(ID: {level["id"]})\n')
        else:
            return

def temporarily(path):
    data = read_json(path)

    for letter in range(200):
        result = {}
        for level in data:
            if letter < len(level["description"]):
                if level["description"][letter] in result:
                    result[level["description"][letter]] += 1
                else:
                    result[level["description"][letter]] = 1
        if result == {}: break
        result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        print(list(result.keys())[0], end='')

print('''Select an action:
               
1 - Remove undefined levels
2 - Count length of JSON
3 - Create backup
4 - Validate JSON
5 - Merge two JSONs
6 - Format JSON
7 - Find level
8 - Sort
9 - Statistics
10 - Count
11 - Find unlisted levels
12 - Crop
13 - Compress
14 - Split
15 - Fix index key
16 - Calculate average difference
17 - Display levels
''')
action = '20719'
# action = input()
print('Path to file:\n')

def add_indent(path):
    print('reading ' + path.split("\\")[-1] + '...')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    print(path.split("\\")[-1] + ' is successfully read')
    with open(path.replace(".json"," (indent).json"), 'w', encoding='utf-8') as f:
        print('writing...')
        json.dump(data, f, indent=4)
    print('successfully writed')
    
for i in range(len(paths)):
    print(f'{i} - {paths[i]}')

input_path = input()
if input_path.isdigit():
    input_path = paths[int(input_path)]
else:
    if not input_path.endswith('.json'): input_path += '.json'
start_time = time()
if action == '1':
    print('''1 - Remove all last
2 - Find undefined levels''')
    pos = input()
    if pos == '1':
        remove_undefined(input_path, True)
    else:
        remove_undefined(input_path, False)
elif action == '2':
    result = count_length(input_path)
    print(f'''Total length: {result[0]}\nExist levels: {result[0] - result[1]} ({round(result[1]/(result[0] + result[1])*100, 2)}%)\nNonexist levels: {result[1]} ({round(result[1]/result[0]*100,2)}%)''')
elif action == '3':
    create_backup(input_path)
elif action == '4':
    validate(input_path)
elif action == '5':
    second_input_path = input()
    if second_input_path.isdigit():
        second_input_path = paths[int(second_input_path)]
    else:
        second_input_path += '.json'
    merge(input_path, second_input_path)
elif action == '6':
    print('''
1 - Format JSON
2 - Add indent
''')
    sub_action = input()
    if sub_action == '1':
        format(input_path)
    else:
        add_indent(input_path)
elif action == '7':
    find(input_path)
elif action == '8':
    sort(input_path)
elif action == '9':
    stat(input_path)
elif action.lower() == '10':
    count(input_path)
elif action.lower() == '11':
    find_unlisted(input_path)
elif action.lower() == '12':
    crop(input_path)
elif action.lower() == '13':
    compress(input_path)
elif action.lower() == '14':
    split_json(input_path)
elif action.lower() == '15':
    format_index(input_path)
elif action.lower() == '16':
    calculate_difference(input_path)
elif action.lower() == '20717':
    display_group(input_path)
elif action.lower() == '20718':
    display_version(input_path)
elif action.lower() == '20719':
    temporarily(input_path)

print(f'\nTime estimated: {time() - start_time}s')