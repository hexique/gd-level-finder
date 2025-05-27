import json

def remove_undefined(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        data: dict = json.load(f)
    keys = list(data.keys())[::-1]
    i = 0
    print(data[keys[0]])
    while data[keys[0]] == None:
        i += 1
        del data[keys[0]]
        print(f'{i}. Removed {keys[0]}')
        del keys[0]
    else:
        print(f'Successfully removed {i} levels')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data))

input_path = input('Path to file:\n')
remove_undefined(input_path)