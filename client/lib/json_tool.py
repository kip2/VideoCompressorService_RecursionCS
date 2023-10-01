import json

def save_json(dic: dict, filepath: str) -> None:
    with open(filepath, "w") as f:
        json.dump(dic, f)

def load_json(filepath: str) -> None:
    with open(filepath, "r") as f:
        d = json.load(f)
    return d

def save_arr_json(arr: list, filepath: str) -> None:
    with open(filepath, "w") as f:
        json.dump(arr, f)

def create_json_file_name(file:str) -> str:
    return file + ".json"

if __name__ == "__main__":
    pass
