# TODO решите задачу
import json


def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)
    total = 0
    for item in data:
        total += item["score"] * item["weight"]
    exactly_total = round(total, 3)
    return exactly_total

print(task())
