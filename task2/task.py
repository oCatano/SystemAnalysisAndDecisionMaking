import csv
import argparse


def _csv_to_graph(filepath):
    data_dict = {}
    with open(filepath, 'r') as table:
        csvreader = csv.reader(table)
        for row in csvreader:
            # print(row)
            if row[0] not in data_dict:
                data_dict[row[0]] = row[1:]
            else:
                data_dict[row[0]].extend(row[1])

    return data_dict


def _get_keys(graph):
    all_keys = []
    for key in graph:
        if key not in all_keys:
            all_keys.append(key)
        for elem in graph[key]:
            if elem not in all_keys:
                all_keys.append(elem)

    return all_keys, len(all_keys)


def _compute_matrix(graph, ln):
    matrix = [[0 for _ in range(ln)] for _ in range(ln)]

    for k in graph:
        for v in graph[k]:
            matrix[int(k) - 1][int(v) - 1] = 1
            matrix[int(v) - 1][int(k) - 1] = -1

    return matrix


def make_csv(matrix, file_name='task_res.csv'):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for row in matrix:
            writer.writerow(row)


def task(filename):
    graph = _csv_to_graph(filename)
    _, ln = _get_keys(graph)
    matrix = _compute_matrix(graph, ln)

    result = [[0 for _ in range(5)] for _ in range(ln)]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                result[i][0] += 1
                for index, value in enumerate(matrix[j]):
                    if value == 1:
                        result[i][2] += 1
            if matrix[i][j] == -1:
                result[i][1] += 1
                for index, value in enumerate(matrix[j]):
                    if value == -1:
                        result[i][3] += 1
                    if value == 1 and index != i:
                        result[i][4] += 1
    make_csv(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('filepath')

    args = parser.parse_args()

    task(args.filepath)
