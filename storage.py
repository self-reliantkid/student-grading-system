from utils import delay
import json

def save_records(info):
    with open("records.json", "w") as file:
        json.dump(info, file)
    print("Saving", end="")
    delay(-1)
    print("\rSaved")


def load_records():
    try:
        with open("records.json", "r") as file:
            return json.load(file) or {}
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}