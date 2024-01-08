import json
import numpy as np


def read_json(file):
    with open(file, 'r') as f:
        a = json.load(f)

    return a


def make_list_from_expert(expert_list):
    expert_list_indexes = []
    expert_list_flatten = []
    position = 0
    for cluster in expert_list:
        if isinstance(cluster, int):
            cluster = [cluster]
        for value in cluster:
            expert_list_indexes.append(position)
            expert_list_flatten.append(value)
        position += 1

    return expert_list_flatten, expert_list_indexes


def make_matrix_from_expert(expert_list):
    expert_list_flatten, expert_list_indexes = make_list_from_expert(expert_list)

    matrix = [[0 for _ in range(len(expert_list_flatten))] for _ in range(len(expert_list_flatten))]

    for i in range(len(expert_list_indexes)):
        for j in range(len(expert_list_indexes)):
            if expert_list_indexes[expert_list_flatten.index(i + 1)] <= expert_list_indexes[
                expert_list_flatten.index(j + 1)]:
                matrix[i][j] = 1

    return matrix


def get_kernel_of_nonequal(matrix_1, matrix_2):
    matrix_1 = np.array(matrix_1)
    matrix_2 = np.array(matrix_2)

    kernel = np.multiply(matrix_1, matrix_2)
    kernel_T = np.multiply(matrix_1.T, matrix_2.T)

    kernel_res = np.logical_or(kernel, kernel_T).astype(np.int32)
    result = []

    for i in range(len(kernel_res)):
        for j in range(len(kernel_res[i])):
            if kernel_res[i][j] == 0:
                pair = sorted([i + 1, j + 1])
                if pair not in result:
                    result.append(pair)

    conc_result = []
    visited = [0 for _ in range(len(result))]

    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            set_1 = set(result[i])
            set_2 = set(result[j])

            if set_1.intersection(set_2):
                visited[i] = 1
                visited[j] = 1
                conc_result.append(list(set_1.union(set_2)))

        if result[i] not in conc_result and visited[i] == 0:
            conc_result.append(result[i])

    print(conc_result)
    return conc_result


def _in_kernel(value, kernel):
    for cluster in kernel:
        if value in cluster:
            return (True, cluster)
    return (False, [])


def make_experted_res_general(expert_1, expert_2, kernel):
    expert_list_flatten_1, expert_list_indexes_1 = make_list_from_expert(expert_1)
    expert_list_flatten_2, expert_list_indexes_2 = make_list_from_expert(expert_2)

    result = []

    for i in range(len(expert_list_flatten_1)):
        if isinstance(expert_1[i], int):
            expert_1[i] = [expert_1[i]]
        for j in range(len(expert_list_flatten_2)):
            pass


def task():
    expert_A = [[1], [2, 3, 4], [5, 6, 7], 8, 9,
                10]
    # read_json(A.json')
    expert_B = [[1, 2, 3], [4, 5], 6, 7, 9,
                [8, 10]]
    # read_json('B.json')
    expert_C = [1, 4, 3, 2, 6, [5, 7, 8], [9, 10]]  # read_json('C.json')
    matrix_A = make_matrix_from_expert(expert_A)
    matrix_B = make_matrix_from_expert(expert_B)
    matrix_C = make_matrix_from_expert(expert_C)
    kernel_AB = get_kernel_of_nonequal(matrix_A, matrix_B)
    kernel_BC = get_kernel_of_nonequal(matrix_B, matrix_C)


if __name__ == '__main__':
    task()
