import json
import pickle
import pandas as pd
import pathlib

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_jsonl(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [json.loads(line) for line in file]

def save_jsonl(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data:
            json.dump(item, file, ensure_ascii=False)
            file.write('\n')

def load_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def save_txt(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)


def load_pickle(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

def save_pickle(data, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

def csv2json(file_path, sep=','):
    df = pd.read_csv(file_path, sep=sep, engine='python')
    json_data = df.to_dict(orient='records')
    return json_data

def json2csv(json_list, out_path):
    df = pd.DataFrame(json_list)
    df.to_csv(out_path, index=False)

def makedirs(path):
    p = pathlib.Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    return path



