import pandas as pd
import sys


# Пример ввода: python3 task.py example.csv 2 2
# Путь нужно указать от той дииректории от которой запускается код

def task(path: str, x, y):
    if path[-3:] == 'csv':
        data = pd.read_csv(path)  # path to csv
        print(data.iloc[x, y])
    else:
        data = pd.read_json(path)  # path to json
        print(data.iloc[x, y])  # choose item
    return True

if __name__ == "__main__":
    task(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
